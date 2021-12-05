from collections import defaultdict
from utils import timer


sign = lambda a: (a > 0) - (a < 0)


def get_data():
    with open("inputs/day5.txt") as f:
        return [
            tuple(tuple(int(y) for y in v.split(",")) for v in x.strip().split(" -> "))
            for x in f
        ]


def list_point_from(line):
    (x1, y1), (x2, y2) = line
    signx, signy = sign(x2 - x1), sign(y2 - y1)
    return (
        (x1 + i * signx, y1 + i * signy)
        for i in range(max(abs(x2 - x1), abs(y2 - y1)) + 1)
    )


def build_vent_count(data, cond=lambda line: True):
    vent_counts = defaultdict(int)
    for line in data:
        if cond(line):
            for pt in list_point_from(line):
                vent_counts[pt] += 1

    return vent_counts


@timer
def part1(data):
    vent_counts = build_vent_count(
        data, lambda line: line[0][0] == line[1][0] or line[0][1] == line[1][1]
    )
    return sum(1 for x in vent_counts.values() if x >= 2)


@timer
def part2(data):
    vent_counts = build_vent_count(data)
    return sum(1 for x in vent_counts.values() if x >= 2)


@timer
def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
