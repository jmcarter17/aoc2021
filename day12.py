from utils import timer
from collections import defaultdict


@timer
def get_data():
    #  Dictionary where each cave has the list of all of its neighbour caves.
    data = defaultdict(set)
    with open("inputs/day12.txt") as f:
        for row in f:
            a, b = row.strip().split("-")
            data[a].add(b)
            data[b].add(a)

    return data


def compute_num_paths(data, cave, visited, can_double_visit=False):
    if cave == "end":
        return 1

    visited = visited | {cave} if cave.islower() else visited

    count = 0
    for neighbour in data[cave]:
        if neighbour not in visited:
            count += compute_num_paths(data, neighbour, visited, can_double_visit)
        elif can_double_visit and neighbour != "start":
            count += compute_num_paths(data, neighbour, visited, False)

    return count


@timer
def part1(data):
    return compute_num_paths(data, "start", set(), False)


@timer
def part2(data):
    return compute_num_paths(data, "start", set(), True)


@timer
def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
