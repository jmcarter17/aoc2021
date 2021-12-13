from utils import timer
import numpy as np


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
    if fold_line[0] == "x":
        x, y = fold_line[1], 2 ** 32
    else:
        x, y = 2 ** 32, fold_line[1]

    for a, b in points:
        if a < x and b < y:
            new_points.add((a, b))
        elif a > x:
            new_points.add((2 * x - a, b))
        elif b > y:
            new_points.add((a, 2 * y - b))

    return new_points


@timer
def part1(data):
    points, folds = data
    points = fold(points, folds[0])
    print(points)

    return len(points)


@timer
def part2(data):
    points, folds = data
    for f in folds:
        points = fold(points, f)

    print(points)

    maxx = max(x for x, _ in points) + 1
    maxy = max(y for _, y in points) + 1

    answer = np.full((maxy, maxx), '.')
    for x, y in points:
        answer[(y, x)] = '#'

    return "\n".join(["".join(x) for x in answer])


@timer
def main():
    data = get_data()
    print(data)
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
