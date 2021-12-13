from functools import reduce
from utils import timer


@timer
def get_data():
    points = set()
    folds = []
    with open("inputs/day13.txt") as f:
        for row in f:
            if "," in row:
                points.add(tuple([int(x) for x in row.strip().split(",")]))
            elif "fold" in row:
                folds.append([row[11:12], int(row[13:].strip())])

    return points, folds


def fold(points, fold_line):
    new_points = set()
    d, p = fold_line

    for a, b in points:
        new_points.add(
            (2 * p - a, b) if d == "x" and a > p
            else (a, 2 * p - b) if d == "y" and b > p
            else (a, b)
        )

    return new_points


@timer
def part1(data):
    points, folds = data
    points = fold(points, folds[0])

    return len(points)


def display_points(points):
    maxx = max(x for x, _ in points) + 1
    maxy = max(y for _, y in points) + 1

    answer = [[" " for _ in range(maxx)] for _ in range(maxy)]

    for x, y in points:
        answer[y][x] = "#"

    return "\n".join(["".join(x) for x in answer])


@timer
def part2(data):
    points, folds = data
    points = reduce(fold, folds, points)

    return display_points(points)


@timer
def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
