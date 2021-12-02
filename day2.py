from itertools import accumulate
import numpy as np
from utils import timer

DIRS = dict(zip("fdu", ((1, 0), (0, 1), (0, -1))))


def parse_row(row):
    d, x = row.split()
    return np.array(DIRS[d[0]]) * int(x)


def get_data():
    with open("inputs/day2.txt") as f:
        return [parse_row(x) for x in f]


def part1(data):
    return np.prod(sum(data))


def part2(data):
    return np.prod((
        sum(x[0] for x in data),
        sum(x[0] * y for (x, y) in zip(data, accumulate(x[1] for x in data)))
    ))


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
