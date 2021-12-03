from collections import Counter
from math import prod


def get_data():
    with open("inputs/day3.txt") as f:
        return [x.strip() for x in f]


def part1(data):
    gamma = "".join([str(int(x.count('1') > len(data)//2)) for x in zip(*data)])
    beta = "".join([str(int(x == '0')) for x in gamma])
    return int(gamma, 2) * int(beta, 2)


def get_oxy_rating(data):
    idx = 0
    while True:
        bits = list(zip(*data))[idx]
        counter = Counter(bits)
        most_common = '0' if counter.get('1', 0) < counter.get('0', 0) else '1'
        data = [x for x in data if x[idx] == most_common]
        idx += 1
        if len(data) == 1:
            return int(data[0], 2)


def get_co2_rating(data):
    idx = 0
    while True:
        bits = list(zip(*data))[idx]
        counter = Counter(bits)
        least_common = '1' if counter.get('0', 0) > counter.get('1', 0) else '0'
        data = [x for x in data if x[idx] == least_common]
        idx += 1
        if len(data) == 1:
            return int(data[0], 2)


def part2(data):
    return prod((get_oxy_rating(data[:]), get_co2_rating(data[:])))


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
