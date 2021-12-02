from itertools import accumulate
from math import prod

DIRS = dict(zip("fdu", ((1, 0), (0, 1), (0, -1))))


def parse_row(row):
    d, scale = row.split()
    d, scale = DIRS[d[0]], int(scale)
    x, y = d
    return x * scale, y * scale


def get_data():
    with open("inputs/day2.txt") as f:
        return [parse_row(x) for x in f]


def part1(data):
    return prod((
        sum(x for (x, _) in data),
        sum(y for (_, y) in data)
    ))


def part2(data):
    return prod((
        sum(x for (x, _) in data),
        sum(x[0] * aim for (x, aim) in zip(data, accumulate(y[1] for y in data))),
    ))


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
