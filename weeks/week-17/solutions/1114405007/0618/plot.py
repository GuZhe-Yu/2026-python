import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os


def main():
    categories = ["Speed", "Memory", "Simplicity", "Stability", "Flexibility"]
    n = len(categories)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    angles += angles[:1]

    scores = {
        "linear_search": [2, 5, 5, 5, 5],
        "binary_search": [4, 5, 3, 2, 1],
        "set_search":    [5, 1, 4, 4, 4],
        "builtin_in":    [4, 5, 5, 5, 5],
        "builtin_bisect":[5, 5, 5, 2, 1],
    }

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    for label, vals in scores.items():
        values = vals + vals[:1]
        ax.plot(angles, values, label=label)
        ax.fill(angles, values, alpha=0.08)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 5)
    ax.set_title("Search Algorithm Radar")
    ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.0))

    os.makedirs("assets", exist_ok=True)
    fig.savefig("assets/radar.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
