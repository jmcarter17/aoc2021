from day1 import get_data, part1, part2


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
