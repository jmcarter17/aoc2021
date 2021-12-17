from itertools import accumulate
from math import sqrt, ceil
from utils import timer, integers_from


@timer
def get_data():
    # return [[20, 30], [-10, -5]]
    return [[282, 314], [-80, -45]]


def max_height(vy):
    return (vy * (vy + 1)) // 2


@timer
def part1(data):
    return max_height(-(data[1][0] + 1))


def vx_gen(init):
    while True:
        yield init
        init = max(0, init - 1)


def vy_gen(init):
    while True:
        yield init
        init -= 1


def find_valid_times(vy, ty):
    ymin, ymax = ty
    ts = integers_from(1)
    ys = accumulate(vy_gen(vy))

    return (t for t, y, _ in zip(ts, ys, range(160)) if ymin <= y <= ymax)


def find_vxmin(xmin):
    return ceil((sqrt(1 + 8 * xmin) - 1) / 2)


def last_x(t, vx):
    *_, (x, _) = zip(accumulate(vx_gen(vx)), range(t))
    return x


def find_all_valid_vx0(vy, tx, ty):
    xmin, xmax = tx
    return (
        vx
        for t in find_valid_times(vy, ty)
        for vx in range(find_vxmin(xmin), xmax + 1)
        if xmin <= last_x(t, vx) <= xmax
    )


@timer
def part2(data):
    ymin = data[1][0]
    init = set(
        (vx, vy) for vy in range(ymin, -ymin) for vx in find_all_valid_vx0(vy, *data)
    )

    return len(init)


@timer
def main():
    data = get_data()

    print(data)
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
