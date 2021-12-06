from utils import timer


def get_data():
    with open("inputs/day6.txt") as f:
        return [int(val) for val in f.read().strip().split(',')]


def reproduction(data, *, numdays):
    for _ in range(numdays):
        reproducing = data.pop(0)
        data.append(reproducing)
        data[6] += reproducing

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
    fishlist = [data.count(i) for i in range(9)]
    print(part1(fishlist[:]))
    print(part2(fishlist[:]))


if __name__ == "__main__":
    main()
