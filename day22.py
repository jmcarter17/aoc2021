from dataclasses import dataclass
from itertools import product, combinations
from math import prod
from typing import Optional

from utils import timer


@timer
def get_data():
    with open("inputs/day22_test.txt") as f:
        return [parse_row(row.strip()) for row in f]


def parse_row(row):
    cmd, rest = row.split(" ")
    coords = tuple(tuple(int(x) for x in coord[2:].split("..")) for coord in rest.split(","))

    return cmd == "on", Cuboid(*coords)


@dataclass(frozen=True, eq=True)
class Cuboid:
    xs: (int, int)
    ys: (int, int)
    zs: (int, int)

    def coords(self) -> tuple[(int, int), (int, int), (int, int)]:
        return self.xs, self.ys, self.zs

    def volume(self) -> int:
        return prod(c[1] - c[0] + 1 for c in self.coords())

    def corners(self) -> iter((int, int, int)):
        return product(self.xs, self.ys, self.zs)

    def intersects(self, other: "Cuboid") -> bool:
        return not (
            any(
                o[0] > s[1] or o[1] < s[0]
                for s, o in zip(self.coords(), other.coords())
            )
        )

    def intersection(self, other: "Cuboid") -> Optional["Cuboid"]:
        if not self.intersects(other):
            return None

        return Cuboid(
            *(
                (max(s[0], o[0]), min(s[1], o[1]))
                for s, o in zip(self.coords(), other.coords())
            )
        )

    def subtract(self, other: "Cuboid") -> set["Cuboid"]:
        if not self.intersects(other):
            return {self}

        intersection = self.intersection(other)
        if intersection == self:
            return set()

        new_cuboids = set()
        (xmin, xmax), (ymin, ymax), (zmin, zmax) = self.coords()
        if self.xs[0] < intersection.xs[0]:
            new_cuboids.add(Cuboid((xmin, intersection.xs[0] - 1), (ymin, ymax), (zmin, zmax)))
            xmin = intersection.xs[0]
        if self.xs[1] > intersection.xs[1]:
            new_cuboids.add(Cuboid((intersection.xs[1] + 1, xmax), (ymin, ymax), (zmin, zmax)))
            xmax = intersection.xs[1]
        if self.ys[0] < intersection.ys[0]:
            new_cuboids.add(Cuboid((xmin, xmax), (ymin, intersection.ys[0] - 1), (zmin, zmax)))
            ymin = intersection.ys[0]
        if self.ys[1] > intersection.ys[1]:
            new_cuboids.add(Cuboid((xmin, xmax), (intersection.ys[1] + 1, self.ys[1]), (zmin, zmax)))
            ymax = intersection.ys[1]
        if self.zs[0] < intersection.zs[0]:
            new_cuboids.add(Cuboid((xmin, xmax), (ymin, ymax), (zmin, intersection.zs[0] - 1)))
        if self.zs[1] > intersection.zs[1]:
            new_cuboids.add(Cuboid((xmin, xmax), (ymin, ymax), (intersection.zs[1] + 1, zmax)))

        return new_cuboids


@timer
def part1(data):
    filtered_data = (
        row for row in data if all(low >= -50 and high <= 50 for low, high in row[1].coords())
    )
    active_cuboids = set()
    for cmd, cuboid in filtered_data:
        new_actives = set()
        for active in active_cuboids:
            new_actives |= active.subtract(cuboid)
        if cmd:
            new_actives.add(cuboid)
        active_cuboids = new_actives
        assert not any(c1.intersects(c2) for c1, c2 in combinations(active_cuboids, 2))

    return sum(cuboid.volume() for cuboid in active_cuboids)


@timer
def part2(data):
    active_cuboids = set()
    for cmd, cuboid in data:
        new_actives = set()
        for active in active_cuboids:
            new_actives |= active.subtract(cuboid)
        if cmd:
            new_actives.add(cuboid)
        active_cuboids = new_actives
        assert not any(c1.intersects(c2) for c1, c2 in combinations(active_cuboids, 2))

    return sum(cuboid.volume() for cuboid in active_cuboids)


@timer
def main():
    data = get_data()
    print(data)
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
