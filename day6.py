from collections import deque
from utils import timer


def get_data():
    with open("inputs/day6.txt") as f:
        return [int(val) for val in f.read().strip().split(',')]


def reproduction(data, *, numdays):
    for _ in range(numdays):
        data.rotate(-1)
        data[6] += data[-1]

    return data


@timer
def part1(fishlist):
    return sum(reproduction(fishlist, numdays=80))


@timer
def part2(fishlist):
    return sum(reproduction(fishlist, numdays=256))


@timer
def main():
    data = get_data()
    fishlist = deque([data.count(i) for i in range(9)])
    print(fishlist)
    print(part1(fishlist.copy()))
    print(part2(fishlist.copy()))


if __name__ == "__main__":
    main()
