from day2 import get_data, part1, part2, main


def test_get_data_benchmark(benchmark):
    data = benchmark(get_data)
    assert len(data)


def test_part1_benchmark(benchmark):
    xs, ys = get_data()
    result = benchmark(part1, xs, ys)
    assert result == 1480518


def test_part2_benchmark(benchmark):
    xs, ys = get_data()
    result = benchmark(part2, xs, ys)
    assert result == 1282809906


def test_main_becnhmark(benchmark):
    benchmark(main)
    assert True
