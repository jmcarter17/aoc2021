from utils import timer


@timer
def get_data():
    with open("inputs/day1.txt") as f:
        return [int(x) for x in f]


def len_increasing(r1, r2):
    return len([None for x, y in zip(r1, r2) if y > x])


@timer
def part1(data):
    return len_increasing(data, data[1:])


@timer
def part2(data):
    return len_increasing(data, data[3:])


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
