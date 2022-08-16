from itertools import product
from math import comb, sqrt
from typing import Iterable

from matplotlib import pyplot as plt

M = 4
N = 3
K = 4


def exact_bits(n: int, max: int) -> Iterable[int]:
    for i in range(max):
        if i.bit_count() == n:
            yield i


if __name__ == "__main__":
    max_combinations = pow(2, M * N)
    n_solutions = comb(M * N, K)
    print(n_solutions)

    grid_rows = round(sqrt(n_solutions))
    grid_cols = round(n_solutions / grid_rows)
    fig = plt.figure(figsize=(16, 12))
    ax = plt.gca()

    offset = 3
    xs_template, ys_template = zip(*product(range(N), range(M)))
    for i, pattern in enumerate(exact_bits(K, max_combinations)):
        row, col = i // grid_rows, i % grid_cols
        xs = [col * (N + offset) + x for x in xs_template]
        ys = [-1 * row * (M + offset) + y for y in ys_template]
        plt.scatter(xs, ys, color="gray", s=16)
        plt.text(
            col * (N + offset) - 0.5,
            -1 * row * (M + offset) + M,
            str(pattern),
        )
        for j, bit in enumerate(f"{pattern:b}".rjust(M * N, "0")):
            if bit == "1":
                x_grid, y_grid = j // M, j % M
                pos = col * (N + offset) + x_grid, -1 * row * (M + offset) + y_grid
                circle = plt.Circle(pos, radius=0.4, color="k", fill=True)
                ax.add_patch(circle)

    plt.axis("off")
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig("patterns.svg")
