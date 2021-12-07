from utils import timer


def get_data():
    with open("inputs/day7.txt") as f:
        return [int(val) for val in f.read().strip().split(",")]


@timer
def part1(data):
    positions = range(min(data), max(data))
    return min(sum((abs(x - pos)) for x in data) for pos in positions)


def realcost(distance):
    return distance * (distance + 1) // 2


@timer
def part2(data):
    positions = range(min(data), max(data))
    return min(sum(realcost(abs(x - pos)) for x in data) for pos in positions)


@timer
def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
