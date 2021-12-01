from utils import timer


@timer
def get_data():
    with open("inputs/day1.txt") as f:
        return [int(x) for x in f]


def count_increasing_adjacent_skip(data, skip):
    return len([None for x, y in zip(data, data[skip:]) if y > x])


@timer
def part1(data):
    return count_increasing_adjacent_skip(data, 1)


@timer
def part2(data):
    return count_increasing_adjacent_skip(data, 3)


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


def test_get_data_benchmark(benchmark):
    data = benchmark(get_data)
    assert len(data)


def test_part1_benchmark(benchmark):
    data = get_data()
    result = benchmark(part1, data)
    assert result == 1527


def test_part2_benchmark(benchmark):
    data = get_data()
    result = benchmark(part2, data)
    assert result == 1575


if __name__ == "__main__":
    main()
