import numpy as np


def parse_row(row):
    info = row.split()
    x = int(info[1])
    dr = (x, 0) if info[0] == 'forward' else (0, x) if info[0] == 'down' else (0, -x)
    return np.array(dr)


def get_data():
    with open("inputs/day2test.txt") as f:
        return [parse_row(x) for x in f]


def part1(data):
    return np.prod(sum(data))


def part2(data):
    aim = 0
    x = 0
    y = 0
    for val in data:
        current = val[0]
        if current == 0:
            aim += val[1]
        else:
            x += current
            y += aim * current

    return x * y


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
