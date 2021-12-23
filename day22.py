from dataclasses import dataclass
from itertools import product
from math import prod
from typing import Optional
from utils import timer


@timer
def get_data():
    with open("inputs/day22.txt") as f:
        return [parse_row(row.strip()) for row in f]


def parse_row(row):
    cmd, rest = row.split(" ")
    coords = tuple(
        tuple(int(x) for x in coord[2:].split("..")) for coord in rest.split(",")
    )

    return cmd == "on", Cuboid(*coords)


@dataclass(frozen=True, eq=True)
class Cuboid:
    xs: (int, int)
    ys: (int, int)
    zs: (int, int)

    def coords(self) -> tuple[(int, int), (int, int), (int, int)]:
        return self.xs, self.ys, self.zs

    def volume(self) -> int:
        return prod(coord[1] - coord[0] + 1 for coord in self.coords())

    def corners(self) -> iter((int, int, int)):
        return product(self.xs, self.ys, self.zs)

    def intersects(self, other: "Cuboid") -> bool:
        return not (
            any(
                you[0] > me[1] or you[1] < me[0]
                for me, you in zip(self.coords(), other.coords())
            )
        )

    def intersection(self, other: "Cuboid") -> Optional["Cuboid"]:
        if not self.intersects(other):
            return None

        return Cuboid(
            *(
                (max(me[0], you[0]), min(me[1], you[1]))
                for me, you in zip(self.coords(), other.coords())
            )
        )


def solve(data):
    accumulator = []
    for cmd, current in data:
        for prev_cmd, previous in accumulator[:]:
            intersection = previous.intersection(current)
            if intersection:
                accumulator.append((not prev_cmd, intersection))
        if cmd:
            accumulator.append((cmd, current))

    return sum((cmd - (not cmd)) * cuboid.volume() for cmd, cuboid in accumulator)


@timer
def part1(data):
    filtered_data = (
        row
        for row in data
        if all(low >= -50 and high <= 50 for low, high in row[1].coords())
    )
    return solve(filtered_data)


@timer
def part2(data):
    return solve(data)


@timer
def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
