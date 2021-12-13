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
    axis, pos = fold_line
    return {
        (2 * pos - a, b) if axis == "x" and a > pos
        else (a, 2 * pos - b) if axis == "y" and b > pos
        else (a, b)
        for a, b in points
    }


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
        answer[y][x] = "█"

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
