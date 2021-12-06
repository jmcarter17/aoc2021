from utils import timer


def get_data():
    with open("inputs/day6_test.txt") as f:
        return [int(val) for val in f.read().strip().split(',')]


@timer
def part1(data):
    for day in range(1, 80+1):
        data = [x - 1 if x > 0 else 6 for x in data] + [8] * data.count(0)

    return len(data)


@timer
def part2(data):
    for day in range(1, 256 + 1):
        data = [x - 1 if x > 0 else 6 for x in data] + [8] * data.count(0)

    return len(data)


@timer
def main():
    data = get_data()
    print(part1(data))
    # print(part2(data))


if __name__ == "__main__":
    main()
