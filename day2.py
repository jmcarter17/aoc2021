import numpy as np


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
    aim = 0
    x = 0
    y = 0
    for val in data:
        aim += val[1]
        x += val[0]
        y += aim * val[0]

    return x * y


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
