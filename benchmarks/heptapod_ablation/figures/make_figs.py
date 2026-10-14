#!/usr/bin/env python3
"""Workflow flowcharts as SVG, Chinese and English. Usage: make_figs.py OUTDIR"""

import sys
from html import escape
from pathlib import Path

C = {
    "agent": ("#16283a", "#5aa9e6"),
    "tool": ("#261f3d", "#a98bf0"),
    "gate": ("#3a3016", "#e7b84b"),
    "good": ("#1d3e2d", "#4fc48a"),
    "bad": ("#4a2423", "#e5645f"),
    "van": ("#3a2618", "#e0864a"),
    "neutral": ("#1d2530", "#4a5668"),
}
TX, MUT, BG = "#e6ebf1", "#a3b1c2", "#0f1318"


def tw(s, fs):
    return sum(fs * (1.0 if ord(ch) > 0x2E80 else 0.56) for ch in s)


class Fig:
    def __init__(self, w, h, lang):
        self.w, self.h, self.lang, self.o = w, h, lang, []
        self.font = (
            '"Noto Sans CJK SC","PingFang SC","Microsoft YaHei",sans-serif'
            if lang == "zh"
            else '"Noto Sans","Segoe UI",Helvetica,Arial,sans-serif'
        )

    def text(self, x, y, s, fs=14, fill=TX, anchor="middle", bold=False, rot=None):
        tr = f' transform="rotate({rot} {x} {y})"' if rot else ""
        fw = ' font-weight="700"' if bold else ""
        self.o.append(
            f'<text x="{x}" y="{y}" font-size="{fs}" fill="{fill}" text-anchor="{anchor}"{fw}{tr}>{escape(s)}</text>'
        )

    def box(self, x, y, w, h, kind, title, lines=(), align="middle", dash=False, tfs=17, lfs=14):
        f, s = C[kind]
        d = ' stroke-dasharray="6 5"' if dash else ""
        self.o.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{f}" stroke="{s}" stroke-width="2"{d}/>'
        )
        n = (1 if title else 0) + len(lines)
        lh = lfs * 1.45
        top = y + h / 2 - ((tfs * 1.3 if title else 0) + lh * len(lines)) / 2
        tx = x + w / 2 if align == "middle" else x + 16
        cy = top
        if title:
            cy += tfs
            self.text(tx, cy, title, tfs, TX, align, True)
            cy += tfs * 0.3
        for ln in lines:
            cy += lh
            self.text(tx, cy - lh * 0.25, ln, lfs, MUT, align)

    def diamond(self, cx, cy, hw, hh, lines, kind="neutral", fs=15):
        f, s = C[kind]
        self.o.append(
            f'<polygon points="{cx},{cy - hh} {cx + hw},{cy} {cx},{cy + hh} {cx - hw},{cy}" fill="{f}" stroke="{s}" stroke-width="2"/>'
        )
        lh = fs * 1.35
        y0 = cy - lh * (len(lines) - 1) / 2 + fs * 0.35
        for i, ln in enumerate(lines):
            self.text(cx, y0 + i * lh, ln, fs, TX, "middle", True)

    def arrow(self, pts, label=None, at=None, color="#8a97a8", dash=False, fs=13.5, lcolor=None):
        d = " ".join(f"{'M' if i == 0 else 'L'}{x},{y}" for i, (x, y) in enumerate(pts))
        da = ' stroke-dasharray="6 5"' if dash else ""
        self.o.append(
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2"{da} marker-end="url(#ah)"/>'
        )
        if label:
            x, y = at or ((pts[0][0] + pts[1][0]) / 2, (pts[0][1] + pts[1][1]) / 2)
            self.label(x, y, label, fs, lcolor or TX)

    def label(self, x, y, s, fs=13.5, fill=TX, rot=None):
        w = tw(s, fs) + 12
        if rot:
            self.o.append(
                f'<rect x="{x - fs * 0.8}" y="{y - w / 2}" width="{fs * 1.6}" height="{w}" rx="4" fill="{BG}"/>'
            )
        else:
            self.o.append(
                f'<rect x="{x - w / 2}" y="{y - fs * 0.85}" width="{w}" height="{fs * 1.6}" rx="4" fill="{BG}"/>'
            )
        self.text(
            x,
            y + fs * 0.35 - (0 if rot else fs * 0.05) + (0 if not rot else 0),
            s,
            fs,
            fill,
            "middle",
            False,
            rot,
        )

    def legend(self, x, y, items):
        for kind, name in items:
            f, s = C[kind]
            self.o.append(
                f'<rect x="{x}" y="{y - 12}" width="16" height="16" rx="3" fill="{f}" stroke="{s}" stroke-width="2"/>'
            )
            self.text(x + 22, y + 1, name, 13.5, MUT, "start")
            x += 22 + tw(name, 13.5) + 22

    def svg(self):
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}" '
            f"font-family='{self.font}'>"
            '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
            '<path d="M0,0 L10,5 L0,10 z" fill="#8a97a8"/></marker></defs>'
            f'<rect width="{self.w}" height="{self.h}" fill="{BG}"/>' + "".join(self.o) + "</svg>"
        )


def T(lang, zh, en):
    return zh if lang == "zh" else en


def fig_overview(lang):
    t = lambda zh, en: T(lang, zh, en)
    f = Fig(1300, 580, lang)
    f.text(
        40,
        40,
        t("整个实验：一次运行从论文到分数", "The experiment: one run, from paper to score"),
        22,
        TX,
        "start",
        True,
    )
    f.box(
        40, 80, 260, 74, "neutral", t("13 篇论文", "13 papers"), [t("LaTeX 源文件", "LaTeX source")]
    )
    f.box(
        40,
        172,
        260,
        74,
        "neutral",
        t("3 个模型", "3 models"),
        ["Sonnet 5 · Haiku 5.5 · Sonnet 5.5"],
    )
    f.box(
        40,
        264,
        260,
        74,
        "neutral",
        t("1 到 3 个 seed", "1 to 3 seeds"),
        [t("同一个任务，重复运行", "the same task, run again")],
    )
    f.arrow([(300, 209), (330, 209), (330, 137), (370, 137)])
    f.arrow([(330, 209), (330, 282), (370, 282)])
    f.label(334, 209, t("同一个任务文字", "same task text"), 12.5, TX, -90)
    f.box(
        370,
        80,
        400,
        114,
        "good",
        t("工具组", "Tools group"),
        [
            t("Claude Code + heptapod 工具（MCP）", "Claude Code + heptapod tools (MCP)"),
            t("+ 协议 + 结束门 + 命令行", "+ protocol + stop gate + shell"),
        ],
    )
    f.box(
        370,
        225,
        400,
        114,
        "van",
        "vanilla",
        [
            t("Claude Code + 命令行", "Claude Code + shell"),
            t("自己运行 FeynRules 和 MadGraph，", "Runs FeynRules and MadGraph itself;"),
            t("自己决定什么时候结束", "decides itself when to stop"),
        ],
    )
    f.box(
        370,
        362,
        400,
        96,
        "neutral",
        t("两组相同", "Same for both groups"),
        [
            t(
                "FeynRules 2.3.49 · MadGraph 3.7.3 · 4 小时时限",
                "FeynRules 2.3.49 · MadGraph 3.7.3 · 4-hour limit",
            ),
            t(
                "每台机器 2 个内核、2 个 agent · 沙箱 · 不能上网",
                "2 kernels, 2 agents per machine · sandbox · no network",
            ),
        ],
        dash=True,
        tfs=15,
        lfs=13,
    )
    f.box(
        815,
        172,
        130,
        74,
        "neutral",
        "model.fr",
        [t("交付的文件", "the delivered file")],
        tfs=16,
        lfs=12.5,
    )
    f.arrow([(770, 137), (790, 137), (790, 196), (815, 196)])
    f.arrow([(770, 282), (790, 282), (790, 222), (815, 222)])
    f.arrow([(945, 209), (985, 209)])
    f.box(985, 80, 285, 270, "neutral", "", [])
    f.text(1127, 110, t("同一个评分器", "One scorer for every run"), 17, TX, "middle", True)
    f.box(
        1000,
        126,
        255,
        112,
        "gate",
        t("① 门：6 项检查", "① Gate: 6 checks"),
        [
            t("编译 · 厄米性 · 动能项", "compile · hermiticity · kinetic"),
            t("质量项 · 质量谱 · MadGraph 导入", "mass · mass spectrum · MG5 import"),
            t("一项失败 → 0 分", "one failure → score 0"),
        ],
        tfs=15,
        lfs=12.5,
    )
    f.box(
        1000,
        250,
        255,
        88,
        "tool",
        t("② 顶点种类 F1", "② Vertex-kind F1"),
        [
            t("和 FeynRules 数据库里", "against the reference model"),
            t("同一篇论文的参考模型比", "of the FeynRules database"),
        ],
        tfs=15,
        lfs=12.5,
    )
    f.arrow([(1127, 350), (1127, 380)])
    f.box(
        985,
        380,
        285,
        175,
        "neutral",
        t("统计", "Statistics"),
        [
            t("每次运行 → 每篇论文一个分数", "Each run → one score per paper"),
            t("每篇论文：对 seed 求平均", "Per paper: mean over seeds"),
            t("工具组 − vanilla，13 篇配对", "Tools − vanilla, 13 papers paired"),
            t("配对置换检验", "Paired permutation test"),
        ],
        tfs=16,
        lfs=13,
    )
    f.text(
        1127,
        543,
        t("三个模型合并：+0.14，p = 0.004", "Three models pooled: +0.14, p = 0.004"),
        15,
        "#4fc48a",
        "middle",
        True,
    )
    f.text(
        40,
        520,
        t(
            "一次运行 = 一个模型 × 一篇论文 × 一个组 × 一个 seed。这次共 182 次。",
            "One run = one model × one paper × one group × one seed. 182 runs in total.",
        ),
        14,
        MUT,
        "start",
    )
    f.text(
        40,
        548,
        t(
            "图 2 是工具组的循环，图 3 是 vanilla 的循环。",
            "Figure 2 shows the tools-group loop; figure 3 shows the vanilla loop.",
        ),
        14,
        MUT,
        "start",
    )
    return f.svg()


def fig_tools(lang):
    t = lambda zh, en: T(lang, zh, en)
    f = Fig(1300, 1040, lang)
    f.text(
        40,
        40,
        t("工具组：agent 的工作循环", "Tools group: the agent's work loop"),
        22,
        TX,
        "start",
        True,
    )
    f.legend(
        560,
        40,
        [
            ("agent", t("agent 的动作", "agent action")),
            ("tool", t("heptapod 工具", "heptapod tool")),
            ("gate", t("harness 的结束门", "harness stop gate")),
            ("good", t("结果", "result")),
        ],
    )
    x0, w0, cx = 60, 420, 270
    f.box(
        x0,
        70,
        w0,
        62,
        "agent",
        t("读论文和 SM.fr", "Read the paper and SM.fr"),
        [t("LaTeX 源文件；SM 的名字不能猜", "LaTeX source; never guess SM names")],
    )
    f.box(
        x0,
        160,
        w0,
        62,
        "agent",
        t("写自检表，再写 model.fr", "Write a self-audit table, then model.fr"),
        [t("FeynRules add-on，加载在 SM.fr 上", "A FeynRules add-on, loaded on top of SM.fr")],
    )
    f.box(
        x0,
        250,
        w0,
        62,
        "tool",
        "lint_model",
        [t("固定规则的检查，毫秒级", "Fixed-rule checks, milliseconds")],
    )
    f.box(
        x0,
        340,
        w0,
        100,
        "tool",
        t("validate_model（预算 10 次）", "validate_model (budget: 10 calls)"),
        [
            t(
                "跑完整检查链，返回到达的阶段和诊断",
                "Runs the full chain; returns the stage and diagnostics",
            ),
            "compile → checks → mg5 → pass",
        ],
    )
    f.diamond(cx, 500, 82, 34, [t("通过？", "Pass?")])
    f.box(
        x0,
        565,
        w0,
        70,
        "tool",
        t("review_model（预算 2 次）", "review_model (budget: 2 calls)"),
        [t("另一个 agent 对照论文审查模型", "A fresh agent checks the model against the paper")],
    )
    f.box(x0, 665, w0, 50, "agent", t("agent 想结束", "The agent tries to stop"), [])
    f.box(
        x0,
        745,
        w0,
        150,
        "gate",
        t("结束门（Stop hook）", "Stop gate (a Stop hook)"),
        [
            t("① model.fr 存在", "1. model.fr exists"),
            t("② 运行过 validate_model", "2. validate_model has run"),
            t("③ 最后一次验证通过", "3. the last validation passed"),
            t("④ 之后 model.fr 没有改过", "4. model.fr has not changed since then"),
        ],
        align="start",
    )
    f.box(x0, 940, w0, 56, "good", t("结束：交付 model.fr", "End: deliver model.fr"), [])
    for a, b in ((132, 160), (222, 250), (312, 340), (440, 466), (635, 665), (715, 745)):
        f.arrow([(cx, a), (cx, b)])
    f.arrow([(cx, 534), (cx, 565)], t("是", "Yes"), (cx + 22, 550))
    f.arrow([(cx, 895), (cx, 940)], t("四项都满足", "all four hold"), (cx, 917))
    # right column
    xr, wr, cr = 650, 460, 880
    f.box(
        xr,
        160,
        wr,
        62,
        "tool",
        t("massbasis（有标量混合时）", "massbasis (when scalars mix)"),
        [t("用 sympy 推导质量基，约 1 秒", "sympy derives the mass basis, about 1 s")],
        dash=True,
    )
    f.arrow([(xr, 191), (480, 191)], dash=True)
    f.box(
        xr,
        440,
        wr,
        120,
        "agent",
        t("读报告，改 model.fr", "Read the report, fix model.fr"),
        [
            t("报告：到达的阶段、每项检查的结论、", "Report: stage reached, each check's verdict,"),
            t(
                "非厄米顶点、质量矩阵、MadGraph 回溯",
                "non-Hermitian vertices, mass matrix, MG5 trace",
            ),
            t(
                "命令行：读自己的 UFO 和日志，跑 wolframscript",
                "Shell: read its own UFO and logs, run wolframscript",
            ),
        ],
        lfs=13.5,
    )
    f.arrow([(352, 500), (xr, 500)], t("否", "No"), (500, 500))
    f.arrow(
        [(cr, 440), (cr, 281), (480, 281)],
        t("再 lint，再验证", "lint and validate again"),
        (cr, 360),
    )
    f.arrow(
        [(480, 600), (770, 600), (770, 560)],
        t("发现改了物理的差异", "a physics change found"),
        (620, 600),
    )
    f.arrow([(480, 820), (cr - 190, 820)], t("有一项不满足", "one does not hold"), (585, 820))
    f.diamond(
        cr,
        820,
        190,
        62,
        [
            t("已经拦了不到 3 次", "Blocked fewer than 3 times"),
            t("而且验证不到 10 次？", "and fewer than 10 validations?"),
        ],
        "gate",
        fs=14.5,
    )
    f.arrow([(cr + 190, 820), (1210, 820), (1210, 500), (xr + wr, 500)])
    f.label(
        1210, 660, t("是：拦回，附上报告摘要", "Yes: send back with a report digest"), 13.5, TX, -90
    )
    f.box(
        xr, 940, wr, 56, "bad", t("放行：带着失败的模型结束", "Allow: end with a failing model"), []
    )
    f.arrow([(cr, 882), (cr, 940)], t("否", "No"), (cr + 22, 910))
    f.text(
        cr,
        1022,
        t(
            "Haiku 工具组的 5 次 0 分都从这里结束。",
            "All 5 zero scores of the Haiku tools group ended here.",
        ),
        13.5,
        MUT,
        "middle",
    )
    f.text(
        60,
        1022,
        t("整个循环有 4 小时时限。", "The whole loop has a 4-hour limit."),
        13.5,
        MUT,
        "start",
    )
    return f.svg()


def fig_vanilla(lang):
    t = lambda zh, en: T(lang, zh, en)
    f = Fig(1300, 470, lang)
    f.text(
        40,
        40,
        t("vanilla：agent 的工作循环", "Vanilla: the agent's work loop"),
        22,
        TX,
        "start",
        True,
    )
    f.box(
        40,
        120,
        230,
        80,
        "van",
        t("读论文和 SM.fr", "Read the paper"),
        [t("LaTeX 源文件", "and SM.fr")],
    )
    f.box(
        310,
        120,
        230,
        80,
        "van",
        t("写 model.fr", "Write model.fr"),
        [t("自己决定怎么写", "its own way")],
    )
    f.box(
        580,
        110,
        330,
        100,
        "van",
        t("自己运行检查", "Run its own checks"),
        [
            t("自己写 wolframscript 脚本，", "Writes its own wolframscript"),
            t("跑 FeynRules 的检查；有时跑 MadGraph", "for the FeynRules checks; sometimes MG5"),
        ],
    )
    f.diamond(1085, 160, 135, 52, [t("自己觉得", "It thinks"), t("通过了？", "it passes?")], "van")
    f.arrow([(270, 160), (310, 160)])
    f.arrow([(540, 160), (580, 160)])
    f.arrow([(910, 160), (950, 160)])
    f.arrow(
        [(1085, 108), (1085, 80), (425, 80), (425, 120)],
        t("否：自己改", "No: fix it itself"),
        (755, 80),
    )
    f.box(
        985, 250, 200, 56, "neutral", t("结束：交付 model.fr", "End: deliver model.fr"), [], tfs=15
    )
    f.arrow([(1085, 212), (1085, 250)], t("是", "Yes"), (1107, 231))
    f.box(
        40,
        250,
        870,
        190,
        "neutral",
        t("和工具组的区别", "The differences from the tools group"),
        [
            t(
                "• 没有 lint、诊断报告、massbasis、审查 agent。",
                "• No lint, no diagnostic report, no massbasis, no referee agent.",
            ),
            t(
                "• 没有结束门：agent 自己判断模型是否通过。",
                "• No stop gate: the agent itself decides if the model passes.",
            ),
            t(
                "• 它的判断可能错：Wprime s2（Sonnet 5）的总结写「全部通过」，",
                '• It can be wrong: in Wprime s2 (Sonnet 5) its summary says "all checks pass",',
            ),
            t(
                "\u00a0\u00a0评分器的质量谱检查失败，分数是 0。",
                "\u00a0\u00a0but the scorer's mass-spectrum check fails, so the score is 0.",
            ),
            t(
                "• 它读很长的日志、反复试错，所以成本是工具组的 2.7 到 3.8 倍。",
                "• It reads long logs and works by trial, so it costs 2.7 to 3.8 times more.",
            ),
        ],
        align="start",
        tfs=16,
        lfs=14,
    )
    return f.svg()


def main():
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in (
        ("workflow_1_overview", fig_overview),
        ("workflow_2_tools_loop", fig_tools),
        ("workflow_3_vanilla_loop", fig_vanilla),
    ):
        for lang in ("zh", "en"):
            (out / f"{name}_{lang}.svg").write_text(fn(lang))
    print(sorted(p.name for p in out.glob("*.svg")))


if __name__ == "__main__":
    main()
