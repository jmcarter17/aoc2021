from utils import timer
import heapq  # Twice as fast as PriorityQueue ... nice.
import math


@timer
def get_data():
    with open("inputs/day15.txt") as f:
        return [[int(c) for c in row.strip()] for row in f]


def shortest_path_cost(risks):
    xlen = len(risks)
    ylen = len(risks[0])

    def get_neighbhours(a, b):
        return [
            (i, j)
            for i, j in ((a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1))
            if 0 <= i < xlen and 0 <= j < ylen
        ]

    lowest_risk = [[math.inf for _ in row] for row in risks]
    lowest_risk[0][0] = 0
    visited = []
    heapq.heappush(visited, (0, (0, 0)))
    while True:
        _, (x, y) = heapq.heappop(visited)
        acc = lowest_risk[x][y]
        if (x, y) == (xlen - 1, ylen - 1):
            return acc
        for x1, y1 in get_neighbhours(x, y):
            new_acc = acc + risks[x1][y1]
            if new_acc < lowest_risk[x1][y1]:
                lowest_risk[x1][y1] = new_acc
                heapq.heappush(visited, (new_acc, (x1, y1)))


@timer
def part1(data):
    return shortest_path_cost(data)


@timer
def part2(data):
    data25 = [
        [(x + i + j - 1) % 9 + 1 for i in range(5) for x in row]
        for j in range(5) for row in data
    ]
    return shortest_path_cost(data25)


@timer
def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
