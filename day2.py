from itertools import accumulate
from math import prod

DIRS = dict(zip("fdu", ((1, 0), (0, 1), (0, -1))))


def parse_row(row):
    d, scale = row.split()
    d, scale = DIRS[d[0]], int(scale)
    x, y = d
    return x * scale, y * scale


def get_data():
    data = ([], [])
    with open("inputs/day2.txt") as f:
        for row in f:
            x, y = parse_row(row)
            data[0].append(x)
            data[1].append(y)

    return data


def part1(xs, ys):
    return prod((sum(xs), sum(ys)))


def part2(xs, ys):
    return prod((
        sum(xs),
        sum(x * aim for (x, aim) in zip(xs, accumulate(ys)))
    ))


def main():
    data = get_data()
    print(part1(*data))
    print(part2(*data))


if __name__ == "__main__":
    main()
