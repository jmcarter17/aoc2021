from utils import timer
import numpy as np
from math import prod


def local_minima(array2d):
    up = np.roll(array2d, 1, 0)
    down = np.roll(array2d, -1, 0)
    left = np.roll(array2d, 1, 1)
    right = np.roll(array2d, -1, 1)
    up[0] = 10
    down[-1] = 10
    left[:, 0] = 10
    right[:, -1] = 10
    return (array2d < up) & (array2d < down) & (array2d < left) & (array2d < right)


def compute_basin_size(data, idx):
    if not (0 <= idx[0] < data.shape[0] and 0 <= idx[1] < data.shape[1]):
        return 0
    if data[idx] == 9:
        return 0

    data[idx] = 9
    return (
        1
        + compute_basin_size(data, (idx[0] + 1, idx[1]))
        + compute_basin_size(data, (idx[0] - 1, idx[1]))
        + compute_basin_size(data, (idx[0], idx[1] + 1))
        + compute_basin_size(data, (idx[0], idx[1] - 1))
    )


@timer
def get_data():
    with open("inputs/day9.txt") as f:
        return np.array([[int(c) for c in row.strip()] for row in f])


@timer
def part1(data):
    mins = local_minima(data)
    return np.sum(mins * (data + 1))


@timer
def part2(data):
    mins = local_minima(data)
    basins = {x: 0 for x in zip(*np.where(mins == 1))}
    for idx in basins:
        basins[idx] = compute_basin_size(data, idx)

    return prod(sorted(basins.values())[-3:])


@timer
def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
