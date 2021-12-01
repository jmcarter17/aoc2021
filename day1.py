from utils import timer


@timer
def get_data():
    with open("inputs/day1.txt") as f:
        return [int(x) for x in f]


@timer
def part1(data):
    return sum(x2 > x1 for x1, x2 in zip(data, data[1:]))


@timer
def part2(data):
    return sum(
        sum((x, y, z)) < sum((y, z, w))
        for x, y, z, w in zip(data, data[1:], data[2:], data[3:])
    )


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
