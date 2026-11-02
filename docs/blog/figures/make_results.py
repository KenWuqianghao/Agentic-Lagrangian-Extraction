"""Figures 4 to 6 of the blog, from the final numbers. Needs matplotlib.

python docs/blog/figures/make_results.py
"""

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
D = json.load(open(ROOT / "benchmarks/heptapod_ablation/hillclimb/models_all.json"))

BG, TX, MUT, GRID = "#0f1318", "#e6ebf1", "#a3b1c2", "#2a313b"
TOOLS, VAN, ZERO = "#3987e5", "#d95926", "#6b7685"
plt.rcParams.update(
    {
        "figure.facecolor": BG,
        "axes.facecolor": BG,
        "savefig.facecolor": BG,
        "text.color": TX,
        "axes.labelcolor": MUT,
        "xtick.color": MUT,
        "ytick.color": MUT,
        "axes.edgecolor": GRID,
        "font.family": "Noto Sans",
        "font.size": 12,
    }
)

MODELS = [
    ("sonnet5", "Sonnet 5\n3 seeds"),
    ("haiku55", "Haiku 5.5\n3 seeds"),
    ("sonnet55", "Sonnet 5.5\n1 seed"),
]


def clean(ax):
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.tick_params(length=0)


# Figure 4: mean score per model, seeds as dots
fig, ax = plt.subplots(figsize=(9, 5.2))
w = 0.34
for i, (k, name) in enumerate(MODELS):
    s = D[k]["summary"]
    for j, (key, col, lab) in enumerate(
        [("shell", TOOLS, "Tools group"), ("vanilla", VAN, "Vanilla")]
    ):
        x = i + (j - 0.5) * (w + 0.03)
        ax.bar(x, s[key], w, color=col, label=lab if i == 0 else None, zorder=2)
        seeds = [p[j] for p in s["seeds"]]
        if len(seeds) > 1:
            ax.scatter(
                [x] * len(seeds), seeds, s=36, color=TX, edgecolor=BG, linewidth=1.5, zorder=3
            )
        ax.text(
            x,
            0.03,
            f"{s[key]:.2f}",
            ha="center",
            va="bottom",
            color=BG,
            fontsize=12,
            weight="bold",
            zorder=4,
        )
    ax.text(
        i,
        max(s["shell"], max(p[0] for p in s["seeds"])) + 0.05,
        f"+{s['diff']:.2f}, p = {s['p']:.3f}",
        ha="center",
        color=TX,
        fontsize=12,
    )
ax.set_xticks(range(3), [m[1] for m in MODELS])
ax.set_ylim(0, 1.0)
ax.set_ylabel("Score (gate × vertex-kind F1), mean over 13 papers")
ax.yaxis.grid(True, color=GRID, zorder=0)
clean(ax)
ax.legend(frameon=False, loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2)
ax.set_title(
    "Tools group vs vanilla, three Claude models (dots = single seeds)",
    loc="left",
    color=TX,
    fontsize=14,
    weight="bold",
    pad=40,
)
fig.text(
    0.01,
    0.01,
    "Pooled over the three models: +0.14, higher on 10 of 13 papers, lower on 1, "
    "paired permutation test p = 0.004.",
    color=MUT,
    fontsize=10.5,
)
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(OUT / "fig4_scores.png", dpi=200)

# Figure 5: pooled per-paper difference
pp = D["pooled"]["per_paper"]
items = sorted(pp.items(), key=lambda kv: kv[1])
fig, ax = plt.subplots(figsize=(9, 6))
cols = [TOOLS if v > 1e-9 else VAN if v < -1e-9 else ZERO for _, v in items]
ax.barh(range(len(items)), [v for _, v in items], color=cols, height=0.62, zorder=2)
for i, (p, v) in enumerate(items):
    lab = "tie (both 1.0)" if abs(v) < 1e-9 else f"{v:+.2f}"
    ax.text(
        v + (0.008 if v >= 0 else -0.008),
        i,
        lab,
        va="center",
        ha="left" if v >= 0 else "right",
        color=TX,
        fontsize=11,
    )
ax.set_yticks(range(len(items)), [p for p, _ in items])
ax.axvline(0, color=MUT, linewidth=1)
ax.set_xlim(-0.12, 0.45)
ax.set_xlabel("Tools group − vanilla, mean over models and seeds")
ax.xaxis.grid(True, color=GRID, zorder=0)
clean(ax)
ax.set_title(
    "Per paper: where the tools group gains",
    loc="left",
    color=TX,
    fontsize=14,
    weight="bold",
    pad=14,
)
fig.tight_layout()
fig.savefig(OUT / "fig5_per_paper.png", dpi=200)

# Figure 6: cost per run
fig, ax = plt.subplots(figsize=(9, 5))
for i, (k, name) in enumerate(MODELS):
    s = D[k]["summary"]
    n = s["chain"][2]
    for j, (col, lab) in enumerate([(TOOLS, "Tools group"), (VAN, "Vanilla")]):
        x = i + (j - 0.5) * (w + 0.03)
        v = s["cost"][j] / n
        ax.bar(x, v, w, color=col, label=lab if i == 0 else None, zorder=2)
        ax.text(x, v + 0.25, f"${v:.2f}", ha="center", color=TX, fontsize=11)
    ax.text(
        i,
        s["cost"][1] / n + 1.6,
        f"vanilla ×{s['cost'][1] / s['cost'][0]:.1f}",
        ha="center",
        color=MUT,
        fontsize=11,
    )
ax.set_xticks(range(3), [m[1] for m in MODELS])
ax.set_ylabel("Cost per run (USD), from Claude Code")
ax.set_ylim(0, 18.5)
ax.yaxis.grid(True, color=GRID, zorder=0)
clean(ax)
ax.legend(frameon=False, loc="upper right")
ax.set_title(
    "Cost per run: the tools group is cheaper on every model",
    loc="left",
    color=TX,
    fontsize=14,
    weight="bold",
    pad=14,
)
fig.tight_layout()
fig.savefig(OUT / "fig6_cost.png", dpi=200)

for k, _ in MODELS:
    s = D[k]["summary"]
    print(
        k,
        s["chain"],
        [round(c / s["chain"][2], 2) for c in s["cost"]],
        round(s["cost"][1] / s["cost"][0], 2),
    )
