from math import sqrt, ceil
from utils import timer


@timer
def get_data():
    # return [[20, 30], [-10, -5]]
    return [[282, 314], [-80, -45]]


def max_height(vy):
    return (vy * (vy + 1)) // 2


@timer
def part1(data):
    return max_height(-(data[1][0] + 1))


def find_valid_times(vy, ty):
    valid_times = []
    ymin, ymax = ty
    t = 0
    y = 0
    while y >= ymin:
        if ymin <= y <= ymax:
            valid_times.append(t)
        t += 1
        y += vy
        vy -= 1
    return valid_times


def find_vxmin(xmin):
    return ceil((sqrt(1 + 8 * xmin) - 1) / 2)


def find_all_valid_vx0(vy, tx, ty):
    valid_times = find_valid_times(vy, ty)
    xmin, xmax = tx
    vx0 = []
    for t in valid_times:
        for vx in range(find_vxmin(xmin), xmax + 1):
            x = 0
            v = vx
            for _ in range(t):
                x += v
                v -= 1 if v else 0
            if xmin <= x <= xmax:
                vx0.append(vx)

    return vx0


@timer
def part2(data):
    ymin = data[1][0]
    init = set((vx, vy) for vy in range(ymin, -ymin) for vx in find_all_valid_vx0(vy, *data))

    return len(init)


@timer
def main():
    data = get_data()

    print(data)
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
