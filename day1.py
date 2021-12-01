def get_data():
    with open("inputs/day1.txt") as f:
        return [int(x) for x in f]


def count_increasing_adjacent_skip(data, skip):
    return len([None for x, y in zip(data, data[skip:]) if y > x])


def part1(data):
    return count_increasing_adjacent_skip(data, 1)


def part2(data):
    return count_increasing_adjacent_skip(data, 3)


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
