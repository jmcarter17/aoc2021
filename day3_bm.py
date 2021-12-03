from day3 import get_data, part1, part2, main


def test_get_data_benchmark(benchmark):
    data = benchmark(get_data)
    assert len(data)


def test_part1_benchmark(benchmark):
    data = get_data()
    result = benchmark(part1, data)
    assert result == 3912944


def test_part2_benchmark(benchmark):
    data = get_data()
    result = benchmark(part2, data)
    assert result == 4996233


def test_main_becnhmark(benchmark):
    benchmark(main)
    assert True
