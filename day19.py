from utils import timer
from collections import defaultdict
from itertools import permutations, product, combinations


@timer
def get_data():
    with open("inputs/day19_test.txt") as f:
        scanners = f.read().split("\n\n")
        return [
            Scanner(
                [
                    Point(*(int(coord) for coord in coords.split(",")))
                    for coords in scanner.split("\n")[1:]
                ]
            )
            for scanner in scanners
        ]


class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y, self.z - other.z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __getitem__(self, item):
        return (self.x, self.y, self.z)[item]

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

    def __hash__(self):
        return hash(str(self))

    def manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)


class Scanner:
    def __init__(self, beacons, location=None):
        self.beacons = beacons
        self.location = location

    def manhattan(self, other):
        return self.location.manhattan(other.location)


def manhattan(x, y):
    return x.manhattan(y)


def get_all_rotations(point):
    rotations = [
        Point(
            point[rotation[0]] * signs[0],
            point[rotation[1]] * signs[1],
            point[rotation[2]] * signs[2],
        )
        for rotation in permutations([0, 1, 2])
        for signs in product([-1, 1], repeat=3)
    ]

    return rotations


def generate_rotations(points):
    rotations = [get_all_rotations(point) for point in points]
    return list(zip(*rotations))


def check_orientation(located_scanner, unlocated_scanner):
    for rotation in generate_rotations(unlocated_scanner.beacons):
        counts = defaultdict(int)

        for point_1 in rotation:
            for point_2 in located_scanner.beacons:
                counts[point_2 - point_1] += 1

        for k in counts:
            if counts[k] == 12:
                return True, Point(k[0], k[1], k[2]), rotation

    return False, None, None


def convert_to_absolute(scanner_location, points):
    return [point + scanner_location for point in points]


@timer
def locate_scanners(scanners):
    n = len(scanners)
    located_scanners = {0: Scanner(scanners[0].beacons, Point(0, 0, 0))}

    while len(located_scanners) != n:
        for i in range(n):
            if i in located_scanners:
                continue

            unlocated_scanner = scanners[i]

            for j in located_scanners:
                located_scanner = located_scanners[j]

                valid, scanner_location, rotation = check_orientation(
                    located_scanner, unlocated_scanner
                )

                if not valid:
                    continue

                newly_located_scanner = Scanner(
                    convert_to_absolute(scanner_location, rotation), scanner_location
                )

                located_scanners[i] = newly_located_scanner

                break

    return located_scanners.values()


@timer
def part1(scanners):
    beacons = {beacon for scanner in scanners for beacon in scanner.beacons}
    return len(beacons)


@timer
def part2(scanners):
    return max(
        manhattan(scanner1, scanner2)
        for scanner1, scanner2 in combinations(scanners, 2)
    )


@timer
def main():
    scanners = get_data()
    located_scanners = locate_scanners(scanners)
    print(part1(located_scanners))
    print(part2(located_scanners))


if __name__ == "__main__":
    main()
