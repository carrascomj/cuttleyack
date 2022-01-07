from pathlib import Path
import matplotlib.pyplot as plt

from cuttleyak import map_groups_to_colors


def plot_colors(alpha=120, beta=50):
    some_groups = [[1, 2, 3], [7, 3, 2, 1], [852, 2492, 2244], [29, 20], [3, 4], [4, 5]]
    color_scale = map_groups_to_colors(some_groups, alpha=alpha, beta=beta)
    print(color_scale)
    flattened = [x for y in color_scale for x in y]
    plt.bar(
        [
            f"G{i}.{j}"
            for i in range(len(some_groups))
            for j in range(len(some_groups[i]))
        ],
        [1] * len(flattened),
        color=flattened,
    )
    plt.xticks(rotation=60)
    plt.savefig(Path("examples") / f"some_colors_a{alpha}_b{beta}.png")


if __name__ == "__main__":
    plot_colors(120, 50)
    plot_colors(5, 120)
