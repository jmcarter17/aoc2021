from utils import timer
import numpy as np
from itertools import product


@timer
def get_data():
    with open("inputs/day11.txt") as f:
        return [[int(x) for x in row.strip()] for row in f]


def get_neighbhours(idx, shape):
    x, y = idx
    return [
        (x + a, y + b)
        for a, b in product([-1, 0, 1], repeat=2)
        if 0 <= x + a < shape[0] and 0 <= y + b < shape[1] and (a, b) != (0, 0)
    ]


def step(data):
    data += 1
    newflashes = data > 9
    oldflashes = data > 9

    while np.any(newflashes):
        for idx in (idx for idx in np.ndindex(data.shape) if newflashes[idx]):
            for n in get_neighbhours(idx, data.shape):
                data[n] += 1

        newflashes = (data > 9) ^ oldflashes
        oldflashes = data > 9

    data *= data <= 9
    return np.sum(data == 0)


@timer
def part1(data):
    return sum(step(data) for _ in range(100))


@timer
def part2(data):
    numsteps = 0
    while np.any(data):
        step(data)
        numsteps += 1

    return numsteps


@timer
def main():
    data = get_data()
    print(part1(np.array(data)))
    print(part2(np.array(data)))


if __name__ == "__main__":
    main()
