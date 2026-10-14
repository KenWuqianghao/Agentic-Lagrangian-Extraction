#!/usr/bin/env python3
"""Build failures.html: every failing or hollow result of the three groups,
with its cause and the lines of the model file or log that show it.

The causes are written here; every snippet is read from the run's files when
the page is built, so a snippet cannot drift from the evidence.

    build_failures_page.py              # writes failures.html (Chinese) next to this file
    build_failures_page.py --lang en    # writes failures.en.html (text from failures_en.py)
"""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cut_statements  # noqa: E402
import failures_en as EN  # noqa: E402

NEW = HERE / "runs"
STORED = Path.home() / "Documents/Github/heptapod/eval/benchmark_runs"
GROUPS = {
    "vanilla": (
        "第 1 组 · vanilla",
        "Claude Code 只有命令行，没有 heptapod",
        lambda p: NEW / p / "rerun/cc_vanilla/s1",
    ),
    "harness": (
        "第 2 组 · harness",
        "cc_sonnet_harness，9 月 30 日的运行",
        lambda p: STORED / p / "rerun/cc_sonnet_harness/s1",
    ),
    "opt": (
        "第 3 组 · 优化后",
        "harness 加上新的检查和提示词",
        lambda p: NEW / p / "rerun/cc_sonnet_opt/s1",
    ),
}


def model(g: str, p: str) -> Path:
    return GROUPS[g][2](p) / "model" / f"{p}_gen.fr"


def lines(path: Path, a: int, b: int) -> str:
    rows = path.read_text(errors="replace").splitlines()
    return "\n".join(f"{n:>4}  {rows[n - 1]}" for n in range(a, min(b, len(rows)) + 1))


def grep(
    path: Path, pattern: str, before: int = 0, after: int = 0, limit: int = 3, width: int = 230
) -> str:
    """The first `limit` matches with context, as numbered lines."""
    if not path.is_file():
        return ""
    rows = path.read_text(errors="replace").splitlines()
    out, last = [], -1
    hits = [i for i, r in enumerate(rows) if re.search(pattern, r)][:limit]
    for i in hits:
        if out and i - before > last + 1:
            out.append("      ...")
        for n in range(max(i - before, last + 1), min(i + after, len(rows) - 1) + 1):
            out.append(f"{n + 1:>4}  {rows[n][:width]}{' ...' if len(rows[n]) > width else ''}")
            last = n
    return "\n".join(out)


def cuts(path: Path, limit: int = 4) -> str:
    rows = path.read_text(errors="replace").splitlines()
    found = cut_statements.cut_lines(path.read_text(errors="replace"))
    out, last = [], None
    for c in found[:limit]:
        n = c["line"]
        if last is not None and n != last + 1:
            out.append("      ...")
        if last is None or n != last + 1:
            out.append(f"{n - 1:>4}  {rows[n - 2][:200]}")
        out.append(f"{n:>4}  {rows[n - 1][:200]}      <-- 这一行不起作用")
        last = n
    if len(found) > limit:
        out.append(f"      ... 还有 {len(found) - limit} 处")
    return "\n".join(out)


def js(path: Path, *keys):
    d = json.loads(path.read_text())
    for k in keys:
        d = d[k]
    return d


def case(g, paper, result, kind, cause, snippets, fix):
    return {
        "group": g,
        "paper": paper,
        "result": result,
        "kind": kind,
        "cause": cause,
        "snippets": [(t, s) for t, s in snippets if s],
        "empty": [t for t, s in snippets if not s],
        "fix": fix,
    }


def build() -> list[dict]:
    van, har, opt = (GROUPS[g][2] for g in ("vanilla", "harness", "opt"))

    def vr(d: Path) -> Path:
        return d / "VALIDATION_REPORT_final.md"

    def h10(p: str, k: int = 10) -> Path:
        return har(p) / "validation" / f"call{k}"

    def oc(p: str, k: int) -> Path:
        return opt(p) / "validation" / f"call{k}"

    C = []

    # Group 1: vanilla.
    C.append(
        case(
            "vanilla",
            "331",
            "compile 失败",
            "agent 知道失败",
            "费米子双线性项里，generation 用了数字，colour 用了自由符号，"
            "index 的数量和类的定义不一致，FeynRules 在展开时报 Inner::incom，然后递归超限。"
            "另外 LTotal 是完整的 Lagrangian，没有写 LSM，评分器又加了一次 LSM。"
            "agent 自己的检查也看到了同样的错误，会话在等待后台任务时结束。",
            [
                (
                    "model.fr：index 数量不对的项",
                    grep(model("vanilla", "331"), r"uRbar\[1,cc\]", 0, 0, 2),
                ),
                ("model.fr：LTotal 没有 LSM", grep(model("vanilla", "331"), r"^LTotal", 0, 1, 1)),
                (
                    "评分器的日志",
                    grep(
                        vr(van("331")), r"Lagrangian: |Inner::incom|RecursionLimit::reclim", 0, 0, 3
                    ),
                ),
            ],
            "一个在限定时间内给出每个检查结论的工具；在任务里说明评分器会自动加 LSM。",
        )
    )
    C.append(
        case(
            "vanilla",
            "ALRM_general",
            "compile 失败",
            "agent 知道失败",
            "hermiticity 检查里出现递归超限。LTotal 是完整的 Lagrangian（自己写了胶子项），"
            "没有 LSM，评分器又加了一次 LSM。"
            "agent 在最后几分钟才第一次用 FeynRules 加载模型，看到了同样的错误，"
            "并且写明模型没有完成。具体是哪一项引起递归，没有确定。",
            [
                ("model.fr：LTotal", grep(model("vanilla", "ALRM_general"), r"^LTotal", 0, 0, 1)),
                (
                    "评分器的日志",
                    grep(vr(van("ALRM_general")), r"Lagrangian: |RecursionLimit", 0, 0, 3),
                ),
                (
                    "agent 的最后一条消息",
                    grep(
                        van("ALRM_general") / "agent_out.md",
                        r"not finished|UFO is not written",
                        0,
                        0,
                        2,
                    ),
                ),
            ],
            "先用一个小模型尽早 compile；报告指出没有展开的顶点。",
        )
    )
    C.append(
        case(
            "vanilla",
            "B-L-SM",
            "hermiticity、mass_spectrum 失败",
            "评分接口",
            "LTotal 用 SM.fr 的各个部分（LGauge、LFermions …）拼出完整的 Lagrangian，"
            "没有出现 LSM 这个符号。评分器看到没有 LSM，就自动加上，"
            "结果 SM 被算了两次，所有 SM 粒子的质量变成 2 倍或 √2 倍。"
            "agent 自己运行的 4 个检查和 MadGraph import 都通过。"
            "这是我的任务提示词漏写了评分规则，不是 agent 的错误。"
            "按原样评分时 mass_spectrum 通过，但是 hermiticity 仍然失败。",
            [
                (
                    "model.fr：LTotal 没有 LSM",
                    grep(model("vanilla", "B-L-SM"), r"^LTotal", 0, 0, 1),
                ),
                (
                    "评分器的日志：质量翻倍",
                    grep(
                        vr(van("B-L-SM")), r"Lagrangian: |HEPTAPOD-MASS\|particle=(t|W)\|", 0, 0, 3
                    ),
                ),
                (
                    "按原样评分的结果",
                    json.dumps(
                        js(van("B-L-SM") / "validation_intent.json", "checks"), ensure_ascii=False
                    ),
                ),
            ],
            "任务里加一句：LTotal 必须包含 LSM，否则评分器会加上。",
        )
    )
    C.append(
        case(
            "vanilla",
            "GeneralU1",
            "mass_spectrum、MadGraph 失败",
            "评分接口 + 没有测试",
            "两个问题。第一，最后一版的 LTotal 没有 LSM，SM 被算两次。第二，"
            "MSphi 在粒子类里声明了一次，又在 M$Parameters 里声明了一次，MadGraph 拒绝。"
            "最后一版从来没有被测试过：agent 的运行在等 Wolfram kernel 的队列里超时了。"
            "它没有运行 WriteUFO 和 MadGraph import。",
            [
                (
                    "model.fr：LTotal 没有 LSM",
                    grep(model("vanilla", "GeneralU1"), r"^LTotal", 0, 0, 1),
                ),
                (
                    "model.fr：MSphi 声明了两次",
                    grep(
                        model("vanilla", "GeneralU1"),
                        r"Mass\s*->\s*\{MSphi|^\s*MSphi\s*==",
                        0,
                        0,
                        2,
                    ),
                ),
                (
                    "评分器的日志",
                    grep(
                        vr(van("GeneralU1")),
                        r"define multiple time|HEPTAPOD-MASS\|particle=d\|",
                        0,
                        0,
                        2,
                    ),
                ),
            ],
            "自己的 kernel；一次 MadGraph import 测试；LSM 的规则。",
        )
    )
    C.append(
        case(
            "vanilla",
            "MDMmodel",
            "mass_spectrum 失败（按原样评分：通过）",
            "评分接口",
            "和 B-L-SM 一样：LTotal 没有 LSM，评分器加了一次，Higgs 部分被算两次，"
            "H 的质量从 125 变成 176.8。"
            "按 agent 写的 LTotal 原样评分时，完整链路通过。但是要注意："
            "这个 LTotal 本身也写成了两行，第二行（Yukawa 和质量项）被截断了，"
            "所以这个“通过”的模型也不完整。",
            [
                (
                    "model.fr：LTotal 没有 LSM",
                    grep(model("vanilla", "MDMmodel"), r"^LTotal", 0, 2, 1),
                ),
                (
                    "评分器的日志",
                    grep(vr(van("MDMmodel")), r"Lagrangian: |HEPTAPOD-MASS\|particle=H\|", 0, 0, 2),
                ),
                (
                    "按原样评分的结果",
                    "full_chain_pass = "
                    + str(js(van("MDMmodel") / "validation_intent.json", "full_chain_pass")),
                ),
            ],
            "LSM 的规则。",
        )
    )
    C.append(
        case(
            "vanilla",
            "Monotops",
            "compile 超时（1350 秒）",
            "模型太大",
            "模型有很多 3×3 的 flavour 张量参数，展开后 1381 项，"
            "hermiticity 检查在时间限制内算不完。"
            "agent 自己的运行等了 20 多分钟也没有结果，它写明没有确认任何一个检查。"
            "具体是哪一项最慢，没有确定。",
            [
                (
                    "model.fr：flavour 张量参数（共十几个）",
                    grep(
                        model("vanilla", "Monotops"),
                        r"Indices\s*->\s*\{Index\[Generation\], Index\[Generation\]\}",
                        2,
                        0,
                        1,
                    ),
                ),
                ("评分器的日志", grep(vr(van("Monotops")), r"terms=|TIMED OUT", 0, 0, 2)),
                (
                    "agent 的最后一条消息",
                    grep(
                        van("Monotops") / "agent_out.md",
                        r"can't yet confirm|cannot yet confirm",
                        0,
                        0,
                        1,
                    ),
                ),
            ],
            "按项给出 hermiticity 的快速反馈；减少 flavour 矩阵的自由元素。",
        )
    )
    C.append(
        case(
            "vanilla",
            "SLQrules",
            "compile 超时（1350 秒）",
            "模型太大",
            "五个 leptoquark 加上全部四次项，展开后有 19509 项。"
            "agent 只成功加载过一次旧版本的文件（有语法错误），"
            "修好后重新运行时任务在队列里被停掉，"
            "所以它从来没有加载过最后的文件。",
            [
                ("评分器的日志", grep(vr(van("SLQrules")), r"terms=|TIMED OUT", 0, 0, 2)),
                ("model.fr：LTotal", grep(model("vanilla", "SLQrules"), r"^LTotal", 0, 0, 1)),
                (
                    "agent 的最后一条消息",
                    grep(van("SLQrules") / "agent_out.md", r"has not been loaded", 0, 0, 1),
                ),
            ],
            "从一开始就有自己的 kernel；在检查之前先报告项数。",
        )
    )
    C.append(
        case(
            "vanilla",
            "SMWeinberg",
            "评分器找不到唯一的总 Lagrangian",
            "评分接口",
            "文件里有两个没有被别的项使用的顶层 L 定义：LTotal，"
            "和 agent 故意留在外面的 LNGGlep（注释里写了“不包含在 LTotal 里”）。"
            "评分器要求只有一个这样的项，所以直接拒绝，没有 compile。agent 自己的 4 个检查、"
            "UFO 和 MadGraph import 都通过。"
            "按原样评分时 4 个检查通过，MadGraph import 失败。",
            [
                (
                    "model.fr：两个顶层的 L 项",
                    grep(
                        model("vanilla", "SMWeinberg"),
                        r"^LNGGlep\s*:=|^LTotal\s*:=|NOT included in LTotal",
                        0,
                        0,
                        3,
                    ),
                ),
                (
                    "按原样评分的结果",
                    json.dumps(
                        {
                            k: js(van("SMWeinberg") / "validation_intent.json", k)
                            for k in ("checks", "madgraph_import_ok")
                        },
                        ensure_ascii=False,
                    ),
                ),
            ],
            "任务里加一句：除了 LTotal 和它的组成部分，不要有别的顶层 L 定义。",
        )
    )
    C.append(
        case(
            "vanilla",
            "pSPSS",
            "hermiticity、kinetic_diagonal、mass_spectrum 失败",
            "agent 知道失败",
            "agent 没有用标准方法声明混合，而是把整个 LSM 展开后用替换规则改写中微子，"
            "再按 θ 的幂次截断。这破坏了共轭项的配对，剩下 39 个非 hermitian 顶点。"
            "n4 的质量是声明值的一半。agent 知道两个检查失败，"
            "写了“如果要我继续请告诉我”就停下了；它还把“质量项是对角的”误读成 mass_spectrum "
            "通过。",
            [
                (
                    "model.fr：改写 LSM 的做法",
                    grep(model("vanilla", "pSPSS"), r"^LSMflav\s*:=|^LTotal\s*=", 0, 0, 2),
                ),
                (
                    "评分器的日志",
                    grep(
                        vr(van("pSPSS")),
                        r"HEPTAPOD-CHECK\|scope=model\|name=(hermiticity|kinetic_diagonal)\|verdict=fail|HEPTAPOD-MASS\|particle=n4",
                        0,
                        0,
                        3,
                        150,
                    ),
                ),
                (
                    "agent 的最后一条消息",
                    grep(van("pSPSS") / "agent_out.md", r"say so|hermiticity check fails", 0, 0, 1),
                ),
            ],
            "标准的混合写法（在 Definitions 里或者用显式的新相互作用项），不要改写 LSM；"
            "把质量表作为数据返回。",
        )
    )

    # Group 2: harness.
    C.append(
        case(
            "harness",
            "SLQrules",
            "compile 失败（10 次调用都失败）",
            "报告没有定位",
            "总 Lagrangian 展开时崩溃（Thread::tdlen，然后递归超限）。报告只给了这两行日志，"
            "没有说是哪个 block。agent 用了 10 次调用都没找到；"
            "其中 4 次是它想做二分查找的文件，被 harness 以“没有总 Lagrangian”拒绝。"
            "我之后用逐个 block 展开的脚本确认：19 个 block 里只有 LQKin 失败。",
            [
                (
                    "model.fr：LQKin 里的写法",
                    grep(model("harness", "SLQrules"), r"DC\[Phi1bar", 0, 0, 1),
                ),
                (
                    "第 10 次调用的日志",
                    grep(
                        h10("SLQrules") / "round0" / "compile.log",
                        r"Thread::tdlen|RecursionLimit",
                        0,
                        0,
                        2,
                    ),
                ),
                (
                    "逐 block 定位的结果（事后运行）",
                    "failing blocks: "
                    + ", ".join(js(HERE / "results" / "compile_bisect_SLQrules.json", "failing"))
                    + "   （共 "
                    f"{js(HERE / 'results' / 'compile_bisect_SLQrules.json', 'blocks')} 个 "
                    "block）",
                ),
            ],
            "compile 失败时逐个 block 展开，报告失败的 block。",
        )
    )
    C.append(
        case(
            "harness",
            "331",
            "mass_spectrum、MadGraph import 失败",
            "报告没有数值",
            "两个问题。第一，Higgs 的 override 改了 vev，"
            "在 Feynman gauge 下 ghost 的质量和声明值不一致；报告只说“mass_spectrum 失败”，"
            "没有给出是哪几行，"
            "agent 的最后一条消息写了“不知道差多少”。第二，14 个质量在粒子类里声明了一次，"
            "又在 M$Parameters 里声明了一次，MadGraph 拒绝；这个错误到第 10 次调用才出现。",
            [
                (
                    "第 10 次调用的日志：只有 ghost 不一致",
                    grep(
                        h10("331") / "round0" / "compile.log",
                        r"HEPTAPOD-MASS\|.*agrees=False",
                        0,
                        0,
                        3,
                    ),
                ),
                (
                    "model.fr：MH2 声明了两次",
                    grep(model("harness", "331"), r"^\s*MH2\s*==|Mass\s*->\s*\{MH2", 0, 0, 2),
                ),
                (
                    "agent 的最后一条消息",
                    grep(har("331") / "agent_out.md", r"magnitude unknown", 0, 0, 1),
                ),
            ],
            "在报告里显示不一致的质量行；只有 ghost 不一致时提示用 unitary gauge；"
            "检查重复声明的参数。",
        )
    )
    C.append(
        case(
            "harness",
            "GeneralU1",
            "kinetic_diagonal 失败（8 次调用）",
            "没有任何工具指出",
            "agent 按协议重新声明了 Higgs doublet（S[11] Phi），"
            "但是把它写成了 M$ClassesDescription 列表后面的一条独立语句。FeynRules 不报错，"
            "直接忽略它。"
            "于是 doublet 没有被旋转，singlet 的动能项里留下一个消不掉的 H–h2 交叉项。"
            "agent 改了 6 次 singlet 的写法，都不在点上。"
            "我把这一段移进列表里、其他不改，模型就通过了完整链路。",
            [
                ("model.fr：类列表在第 81 行结束", lines(model("harness", "GeneralU1"), 79, 81)),
                ("model.fr：Phi 的声明在列表外面", lines(model("harness", "GeneralU1"), 271, 279)),
                (
                    "第 10 次调用的日志",
                    grep(
                        h10("GeneralU1") / "round0" / "compile.log",
                        r"Non diagonal kinetic term found",
                        0,
                        0,
                        1,
                    ),
                ),
                (
                    "移进列表后的真实运行",
                    json.dumps(
                        {
                            k: js(HERE / "results" / "GeneralU1_class_inside.json", k)
                            for k in ("full_chain_pass", "checks")
                        },
                        ensure_ascii=False,
                    ),
                ),
            ],
            "lint：类声明写在 M$ClassesDescription 外面。",
        )
    )
    C.append(
        case(
            "harness",
            "SMWeinberg",
            "hermiticity 失败（10 次调用都失败）",
            "报告只指出了类别",
            "l 这个场有两个 index（spin、generation）。写成 l[ff] 时，FeynRules 从左边填，"
            "ff 被当成 spin index。结果是 16 个化简不了的顶点。"
            "+ HC[...] 是有的，所以报告里“通常是缺少 HC”的提示是错的方向。"
            "报告说了“显式的 spin 或 flavour index”，但是没有说 ff 落在 spin 位置；"
            "lint 没有发现。",
            [
                (
                    "model.fr：l[ff] 的写法",
                    grep(model("harness", "SMWeinberg"), r"\bl\[ff\]", 0, 0, 3),
                ),
                (
                    "第 10 次调用的报告",
                    grep(h10("SMWeinberg") / "agent_report.md", r"UNREDUCED", 0, 0, 1),
                ),
                (
                    "第 10 次调用的日志：ff 在 Spin 位置",
                    grep(
                        h10("SMWeinberg") / "round0" / "compile.log",
                        r"HEPTAPOD-HERM\|i=1\|",
                        0,
                        0,
                        1,
                        260,
                    ),
                ),
            ],
            "lint：费米子场给了一部分 index。",
        )
    )
    C.append(
        case(
            "harness",
            "ALRM_general",
            "没有交付模型",
            "不是验证链的问题",
            "agent 在第一次写文件之前，一条回复就用完了 64000 的输出 token "
            "上限（几乎全部是思考）。会话以 API 错误结束，Stop gate 也不会触发。",
            [
                (
                    "run.json",
                    str(js(har("ALRM_general") / "run.json", "agent", "api_error"))[:200]
                    if (har("ALRM_general") / "run.json").is_file()
                    else "",
                )
            ],
            "提高输出上限，或者要求分段写文件。",
        )
    )
    C.append(
        case(
            "harness",
            "Monotops",
            "链路通过，但是是空的",
            "被截断的语句",
            "LTotal 的定义在第一行的行尾已经是完整的表达式，"
            "后面以 + 开头的行被 Mathematica 当成另一条语句，不起作用。"
            "所有新的相互作用项都在被丢掉的行里。UFO 只有 SM 的 163 个顶点，"
            "6 个新粒子没有任何顶点。4 个检查和 MadGraph 都通过，"
            "referee 读 .fr 的文字也说没有问题。",
            [
                ("model.fr：被截断的地方", cuts(model("harness", "Monotops"), 2)),
                ("UFO 里新粒子的顶点数", "163 个顶点，其中包含新粒子的：0"),
            ],
            "检测被截断的语句；新粒子没有顶点时判为失败。",
        )
    )
    C.append(
        case(
            "harness",
            "pSPSS",
            "链路通过，但是是空的",
            "被截断的语句 + index",
            "两个问题叠在一起：l[ff] 的 index 问题（前 9 次调用 hermiticity 一直失败），"
            "和被截断的语句。第 10 次调用时带重中微子的项从 Lagrangian 里消失了"
            "（532 项变成 496 项），hermiticity 因为这些项不见了而通过。UFO 里没有任何包含 n4、"
            "n5 的顶点。",
            [
                ("model.fr：被截断的地方", cuts(model("harness", "pSPSS"), 2)),
                (
                    "model.fr：l[ff] 仍然在文件里",
                    grep(model("harness", "pSPSS"), r"\bl\[ff\]", 0, 0, 2),
                ),
                (
                    "第 9、10 次调用的项数",
                    grep(
                        h10("pSPSS", 9) / "round0" / "compile.log", r"HEPTAPOD-LAGRANGIAN", 0, 0, 1
                    )
                    + "\n"
                    + grep(
                        h10("pSPSS", 10) / "round0" / "compile.log", r"HEPTAPOD-LAGRANGIAN", 0, 0, 1
                    ),
                ),
            ],
            "同上，加上 index 数量检查。",
        )
    )
    C.append(
        case(
            "harness",
            "ChernSimonsPortal",
            "链路通过，有一处被截断",
            "被截断的语句",
            "有一条顶层语句的续行以 + 或 - 开头，被丢掉。新粒子仍然有顶点，所以不是空的通过，"
            "但是模型比 agent 写的少了一部分。",
            [("model.fr：被截断的地方", cuts(model("harness", "ChernSimonsPortal"), 2))],
            "检测被截断的语句。",
        )
    )

    # Group 3: optimised.
    C.append(
        case(
            "opt",
            "ALRM_general",
            "hermiticity 失败（10 次调用）",
            "被截断的语句",
            "LHp2 和 LA2 的定义写成多行，第一行的行尾已经是完整的表达式，所以后面的共轭项被丢掉。"
            "报告指出了 block 的名字（LHp2），"
            "但是给的提示是“缺少 HC”，没有说这个 block 只剩下 18 项里的 3 项。"
            "agent 换了 7 种理论，每次都保留了多行的写法。",
            [
                (
                    "第 10 次调用的 model.fr：被截断的地方",
                    cuts(oc("ALRM_general", 10) / "model.fr", 2),
                ),
                (
                    "第 10 次调用的日志：LHp2 只剩第一行的内容",
                    grep(
                        oc("ALRM_general", 10) / "round0" / "compile.log",
                        r"HEPTAPOD-HERMBLOCK\|block=LHp2",
                        0,
                        0,
                        1,
                    ),
                ),
                (
                    "agent 的话",
                    grep(
                        opt("ALRM_general") / "agent_out.md",
                        r"can't say which|cannot say which",
                        0,
                        0,
                        1,
                    ),
                ),
            ],
            "检测被截断的语句。",
        )
    )
    C.append(
        case(
            "opt",
            "MDMmodel",
            "mass 检查、MadGraph import 失败（只用了 3 次调用）",
            "agent 拒绝继续",
            "这次 agent 保留了论文里的 t–T 混合项（第 2 组为了通过把它删掉了）。"
            "这一项让质量矩阵不对角，文件里没有对 top 部分做旋转。报告准确地指出了这一项。"
            "agent 三次被 Stop gate 拦住，每次都回答“需要你来决定”，没有调用任何工具，"
            "第四次因为达到继续次数上限被放行。还剩 7 次验证没有用。",
            [
                (
                    "第 3 次调用的日志",
                    grep(
                        oc("MDMmodel", 3) / "round0" / "compile.log",
                        r"Non diagonal mass term found",
                        0,
                        0,
                        1,
                    ),
                ),
                (
                    "Stop gate 的记录",
                    "\n".join(
                        f"{x.get('decision')}: validations={x.get('validations')} "
                        f"continuations_before={x.get('continuations_before')}  "
                        f"{str(x.get('why'))[:70]}"
                        for x in map(
                            json.loads,
                            (opt("MDMmodel") / "stop_gate_log.jsonl").read_text().splitlines(),
                        )
                    ),
                ),
                (
                    "agent 的最后一条消息",
                    grep(
                        opt("MDMmodel") / "agent_out.md",
                        r"need from you|Choose one|stopping here",
                        0,
                        0,
                        2,
                    ),
                ),
            ],
            "给出重新声明第三代夸克的方法；Stop gate 需要处理“拒绝继续”的情况。",
        )
    )
    C.append(
        case(
            "opt",
            "SLQrules",
            "compile 超时（1350 秒）",
            "模型太大",
            "前 4 次调用是崩溃（SU(2) index 放错了位置），agent 在第 5 次自己找到了原因。"
            "之后完整的模型 compile 超过 1350 秒；"
            "去掉 Yukawa 和高次项的版本 185 秒能 compile，但是 leptoquark 的质量混合没有旋转，"
            "mass_diagonal 失败。报告只说“超时，可能需要化简”，没有每个 block 的时间。",
            [
                (
                    "每次调用的结果",
                    "\n".join(
                        f"call {k}: {js(oc('SLQrules', k) / 'summary.json', 'stage')}  "
                        f"{js(oc('SLQrules', k) / 'summary.json', 'seconds')} s"
                        for k in range(1, 9)
                        if (oc("SLQrules", k) / "summary.json").is_file()
                    ),
                ),
                (
                    "第 7 次调用的日志（去掉大部分项之后）",
                    grep(
                        oc("SLQrules", 7) / "round0" / "compile.log",
                        r"Non diagonal mass term found",
                        0,
                        0,
                        1,
                    ),
                ),
            ],
            "报告每个 block 的时间；质量混合的旋转方法。",
        )
    )
    C.append(
        case(
            "opt",
            "GeneralU1",
            "链路通过，但是 3 个新粒子没有顶点",
            "被截断的语句",
            "这次 Phi 的声明在列表里面，kinetic_diagonal 通过了。但是 LTotal 的第二行被丢掉："
            "重中微子的项、所有 Z′–费米子耦合和 Z′ 的质量项都不在 UFO 里。"
            "新的检查在第 3 次调用就报告了“n1、n2、n3 没有顶点”，但是它的提示指向“index 不完整”，"
            "方向是错的。agent 之后用了 7 次调用都没找到真正的原因。",
            [
                ("model.fr：被截断的地方", cuts(model("opt", "GeneralU1"), 2)),
                (
                    "最后一次循环内的结论",
                    str(js(opt("GeneralU1") / "run.json", "agent", "last_inloop", "stage")),
                ),
                (
                    "agent 的最后一条消息",
                    grep(
                        opt("GeneralU1") / "agent_out.md",
                        r"is dropped|are dropped|no vertex",
                        0,
                        0,
                        1,
                    ),
                ),
            ],
            "检测被截断的语句；“没有顶点”的报告不要猜原因。",
        )
    )
    C.append(
        case(
            "opt",
            "Monotops",
            "链路通过，但是 4 个新粒子没有顶点",
            "被截断的语句",
            "和 GeneralU1 一样：所有相互作用项都在 LTotal 被丢掉的第二行里。"
            "第 7 次调用时 agent 偶然把两项移到第一行，那两个粒子就有了顶点；第 8 次又移回去，"
            "顶点又消失了。"
            "同时“UFO 参数重复定义”的报告只列了 20 个名字，给的两个原因都不对，"
            "agent 在上面花了 7 次调用。",
            [
                ("model.fr：被截断的地方", cuts(model("opt", "Monotops"), 2)),
                (
                    "最后一次循环内的结论",
                    str(js(opt("Monotops") / "run.json", "agent", "last_inloop", "stage")),
                ),
            ],
            "检测被截断的语句。",
        )
    )
    C.append(
        case(
            "opt",
            "331",
            "链路通过，有 9 处被截断",
            "被截断的语句",
            "链路通过了，新粒子也都有顶点，但是有 9 条语句的续行被丢掉："
            "8 行 Yukawa 项和一个质量项不在 UFO 里。referee 读文字时把这些 Yukawa "
            "行当作“已经实现”。",
            [("model.fr：被截断的地方（前 3 处）", cuts(model("opt", "331"), 3))],
            "检测被截断的语句。",
        )
    )
    C.append(
        case(
            "opt",
            "SMWeinberg",
            "链路通过，有 1 处被截断",
            "被截断的语句",
            "这次 agent 从第一次调用就给了费米子全部的 index，hermiticity 通过。"
            "但是 LTotal 有一行续行被丢掉，3 个 Goldstone 项不在 UFO 里。",
            [("model.fr：被截断的地方", cuts(model("opt", "SMWeinberg"), 2))],
            "检测被截断的语句。",
        )
    )
    return C


CSS = """
:root{--bg:#f7f6f2;--fg:#1f2328;--mut:#5e6570;--card:#fff;--line:#dcd9d0;--code:#f1efe8;--acc:#9a3412;--ok:#166534;
--k1:#7c2d12;--k2:#1e3a8a;--k3:#14532d}
@media (prefers-color-scheme:dark){:root{--bg:#16181c;--fg:#e6e4dd;--mut:#9aa1ab;--card:#1e2126;--line:#33383f;--code:#111317;--acc:#fdba74;--ok:#86efac;
--k1:#fdba74;--k2:#93c5fd;--k3:#86efac}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 system-ui,-apple-system,"PingFang SC","Noto Sans CJK SC","Microsoft YaHei",sans-serif}
main{max-width:1000px;margin:0 auto;padding:28px 20px 80px}
h1{font-size:26px;margin:0 0 6px}h2{font-size:20px;margin:40px 0 4px;padding-top:12px;border-top:2px solid var(--line)}
.sub{color:var(--mut);margin:0 0 18px}.note{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--acc);padding:12px 16px;border-radius:6px;margin:14px 0}
table{border-collapse:collapse;width:100%;margin:12px 0;font-size:15px;font-variant-numeric:tabular-nums}
th,td{border-bottom:1px solid var(--line);padding:7px 10px;text-align:left}th{color:var(--mut);font-weight:600}td.n{text-align:right}
nav{position:sticky;top:0;background:var(--bg);padding:10px 0;border-bottom:1px solid var(--line);z-index:2;display:flex;gap:8px;flex-wrap:wrap}
nav button{font:inherit;font-size:14px;padding:5px 12px;border-radius:999px;border:1px solid var(--line);background:var(--card);color:var(--fg);cursor:pointer}
nav button[aria-pressed=true]{background:var(--fg);color:var(--bg);border-color:var(--fg)}
article{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:16px 18px;margin:14px 0}
article h3{margin:0 0 2px;font-size:18px}article .res{color:var(--acc);font-weight:600}
.tag{display:inline-block;font-size:12.5px;padding:1px 9px;border-radius:999px;border:1px solid currentColor;margin-left:8px;vertical-align:2px}
.g-vanilla .tag{color:var(--k1)}.g-harness .tag{color:var(--k2)}.g-opt .tag{color:var(--k3)}
article p{margin:8px 0}.lab{font-size:13.5px;color:var(--mut);margin:12px 0 3px;font-weight:600}
pre{background:var(--code);border:1px solid var(--line);border-radius:6px;padding:10px 12px;margin:0;overflow-x:auto;font:13px/1.5 ui-monospace,"SF Mono",Menlo,Consolas,monospace;white-space:pre}
.fix{border-top:1px dashed var(--line);margin-top:12px;padding-top:8px}.fix b{color:var(--ok)}
footer{color:var(--mut);font-size:14px;margin-top:40px}
"""  # noqa: E501

JS = """
const bs=[...document.querySelectorAll('nav button')];
bs.forEach(b=>b.onclick=()=>{bs.forEach(x=>x.setAttribute('aria-pressed',x===b));
document.querySelectorAll('section[data-g]').forEach(s=>s.hidden=!(b.dataset.g==='all'||s.dataset.g===b.dataset.g));});
"""


def to_english(cases: list[dict]) -> list[dict]:
    out = []
    for c in cases:
        result, kind, cause, fix = EN.CASES[(c["group"], c["paper"])]
        snippets = []
        for label, snip in c["snippets"]:
            for pat, repl in EN.INLINE:
                snip = re.sub(pat, repl, snip)
            snippets.append(
                (EN.LABELS[label] if re.search(r"[\u4e00-\u9fff]", label) else label, snip)
            )
        out.append(
            {**c, "result": result, "kind": kind, "cause": cause, "fix": fix, "snippets": snippets}
        )
    return out


def render_en(cases: list[dict]) -> str:
    page = render(to_english(cases))
    ui = EN.UI
    swaps = [
        ("lang='zh-CN'", "lang='en'"),
        ("每个失败的例子：原因和片段", ui["title"]),
        (
            "Sonnet，16 篇论文，每组 1 个 seed，同一个评分器。"
            "片段是生成这个页面时从运行的文件里读出来的。",
            ui["sub"],
        ),
        (
            "<th>组</th><th>完整链路通过</th><th>通过并且模型是实的</th><th>本页的例子</th>",
            "".join(f"<th>{x}</th>" for x in ui["th"]),
        ),
        ("第 1 组 · vanilla（只有命令行）", ui["rows"][0]),
        ("第 2 组 · harness（cc_sonnet_harness）", ui["rows"][1]),
        ("<td>第 3 组 · 优化后</td>", f"<td>{ui['rows'][2]}</td>"),
        (
            "“模型是实的”：链路通过，并且没有被截断的语句，并且每个新粒子在 UFO 里至少有一个顶点。"
            "本页包括两类例子：没有通过链路的，和通过了但是模型是空的或者不完整的。",
            ui["note1"],
        ),
        (
            "<b>被截断的语句</b>是三个组里最常见的隐藏问题。在 .fr 文件里，"
            "一条顶层语句如果在行尾已经是完整的表达式，"
            "Mathematica 就在那里结束它；下一行以 + 或 - 开头的部分是另一条语句，不起作用。"
            "FeynRules、4 个检查和 MadGraph 都不报告。",
            ui["note2"],
        ),
        (">全部<", f">{ui['all']}<"),
        ("<b>需要什么：</b>", f"<b>{ui['needs']}</b>"),
        (
            "来源：benchmarks/heptapod_ablation/GROUPS.md 和 results/forensics/ 下的三份分析。"
            "原因的文字来自这些分析；标为“没有确定”的地方是真的没有确定。每组只有一个 seed。",
            ui["footer"],
        ),
    ]
    for g, (zh_title, zh_desc, _fn) in GROUPS.items():
        swaps += [
            (html.escape(zh_title), ui["groups"][g][0]),
            (html.escape(zh_desc), ui["groups"][g][1]),
        ]
    for a, b in swaps:
        if a not in page:
            raise KeyError(f"English page: text not found: {a[:40]}")
        page = page.replace(a, b)
    page = page.replace("）</button>", ")</button>").replace("（", " (")
    left = re.findall(r"[\u4e00-\u9fff]+", page)
    if left:
        raise ValueError(f"English page still has Chinese text: {left[:5]}")
    return page


def render(cases: list[dict]) -> str:
    e = html.escape
    counts = {g: sum(c["group"] == g for c in cases) for g in GROUPS}
    out = [
        "<!doctype html><html lang='zh-CN'><meta charset='utf-8'><meta name='viewport' "
        "content='width=device-width,initial-scale=1'>",
        "<title>每个失败的例子：原因和片段</title><style>",
        CSS,
        "</style><main>",
        "<h1>每个失败的例子：原因和片段</h1>",
        "<p class='sub'>Sonnet，16 篇论文，每组 1 个 seed，同一个评分器。"
        "片段是生成这个页面时从运行的文件里读出来的。</p>",
        "<table><tr><th>组</th><th>完整链路通过</th><th>通过并且模型是实的</th><th>本页的例子</th></tr>",
        "<tr><td>第 1 组 · vanilla（只有命令行）</td><td class='n'>7 / 16</td><td "
        f"class='n'>7</td><td class='n'>{counts['vanilla']}</td></tr>",
        "<tr><td>第 2 组 · harness（cc_sonnet_harness）</td><td class='n'>11 / 16</td><td "
        f"class='n'>8</td><td class='n'>{counts['harness']}</td></tr>",
        "<tr><td>第 3 组 · 优化后</td><td class='n'>13 / 16</td><td class='n'>9</td><td "
        f"class='n'>{counts['opt']}</td></tr></table>",
        "<div class='note'>“模型是实的”：链路通过，并且没有被截断的语句，"
        "并且每个新粒子在 UFO 里至少有一个顶点。"
        "本页包括两类例子：没有通过链路的，和通过了但是模型是空的或者不完整的。</div>",
        "<div class='note'><b>被截断的语句</b>是三个组里最常见的隐藏问题。在 .fr 文件里，"
        "一条顶层语句如果在行尾已经是完整的表达式，"
        "Mathematica 就在那里结束它；下一行以 + 或 - 开头的部分是另一条语句，不起作用。"
        "FeynRules、4 个检查和 MadGraph 都不报告。</div>",
        "<nav><button data-g='all' aria-pressed='true'>全部</button>",
    ]
    out += [
        f"<button data-g='{g}' aria-pressed='false'>{e(GROUPS[g][0])}（{counts[g]}）</button>"
        for g in GROUPS
    ]
    out.append("</nav>")
    for g, (title, desc, _fn) in GROUPS.items():
        out.append(
            f"<section data-g='{g}' class='g-{g}'><h2>{e(title)}</h2><p class='sub'>{e(desc)}</p>"
        )
        for c in (x for x in cases if x["group"] == g):
            out.append(
                f"<article><h3>{e(c['paper'])}<span class='tag'>{e(c['kind'])}</span></h3>"
                f"<div class='res'>{e(c['result'])}</div><p>{e(c['cause'])}</p>"
            )
            for label, snip in c["snippets"]:
                out.append(f"<div class='lab'>{e(label)}</div><pre>{e(snip)}</pre>")
            out.append(f"<div class='fix'><b>需要什么：</b>{e(c['fix'])}</div></article>")
        out.append("</section>")
    out += [
        "<footer>来源：benchmarks/heptapod_ablation/GROUPS.md 和 results/forensics/ 下的三份分析。"
        "原因的文字来自这些分析；标为“没有确定”的地方是真的没有确定。每组只有一个 seed。</footer>",
        "</main><script>",
        JS,
        "</script></html>",
    ]
    return "".join(out)


def main() -> int:
    cases = build()
    for c in cases:
        if c["empty"]:
            print(f"EMPTY snippet: {c['group']} {c['paper']}: {c['empty']}", file=sys.stderr)
    if "--lang" in sys.argv and sys.argv[sys.argv.index("--lang") + 1] == "en":
        (HERE / "failures.en.html").write_text(render_en(cases))
        print(f"wrote {HERE / 'failures.en.html'} ({len(cases)} cases)")
        return 0
    (HERE / "failures.html").write_text(render(cases))
    print(f"wrote {HERE / 'failures.html'} ({len(cases)} cases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
