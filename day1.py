from utils import timer


@timer
def get_data():
    with open("inputs/day1.txt") as f:
        return [int(x) for x in f]


@timer
def part1(data):
    return len([None for x1, x2 in zip(data, data[1:]) if x2 > x1])


@timer
def part2(data):
    return len([None for x, y in zip(data, data[3:]) if y > x])


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
