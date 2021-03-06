from itertools import combinations

from day22 import Cuboid, parse_row, part1, part2


def test_cuboid_volume():
    assert Cuboid((10, 12), (10, 12), (10, 12)).volume() == 27
    assert Cuboid((1, 100), (1, 100), (1, 100)).volume() == 1000000
    assert Cuboid((1, 1), (1, 1), (1, 1)).volume() == 1
    assert Cuboid((1, 0), (1, 1), (1, 1)).volume() == 0


def test_cuboid_corners():
    assert list(Cuboid((10, 12), (10, 12), (10, 12)).corners()) == [
        (10, 10, 10),
        (10, 10, 12),
        (10, 12, 10),
        (10, 12, 12),
        (12, 10, 10),
        (12, 10, 12),
        (12, 12, 10),
        (12, 12, 12),
    ]


def test_cuboid_intersects():
    cuboid1 = Cuboid((10, 12), (10, 12), (10, 12))
    cuboid2 = Cuboid((9, 11), (9, 11), (9, 11))
    cuboid3 = Cuboid((10, 10), (10, 10), (10, 10))
    cuboid4 = Cuboid((0, 9), (0, 9), (0, 9))

    assert cuboid1.intersects(cuboid2)
    assert cuboid1.intersects(cuboid3)
    assert not cuboid1.intersects(cuboid4)


def test_cuboid_intersection():
    cuboid1 = Cuboid((10, 12), (10, 12), (10, 12))
    cuboid2 = Cuboid((9, 11), (9, 11), (9, 11))
    cuboid3 = Cuboid((10, 10), (10, 10), (10, 10))
    cuboid4 = Cuboid((0, 9), (0, 9), (0, 9))

    assert cuboid1.intersection(cuboid2) == Cuboid((10, 11), (10, 11), (10, 11))
    assert cuboid1.intersection(cuboid3) == cuboid3
    assert cuboid1.intersection(cuboid4) is None


def test_part1_part2():
    with open("inputs/day22_test.txt") as f:
        data = [parse_row(row.strip()) for row in f]

    assert part1(data) == 474140
    assert part2(data) == 2758514936282235

