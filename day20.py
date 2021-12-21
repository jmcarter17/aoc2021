from utils import timer


@timer
def get_data():
    with open("inputs/day20.txt") as f:
        algorithm = [int(c == "#") for c in f.readline().strip()]
        f.readline()
        image_raw = [list(row.strip()) for row in f]
        image = {
            (i, j)
            for i, row in enumerate(image_raw)
            for j, c in enumerate(row)
            if c == "#"
        }

        return algorithm, image


def get_index(image, cur_idx, infinite_value, xmin, xmax, ymin, ymax):
    i, j = cur_idx
    idx = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            idx = idx << 1 | (
                (int((x, y) in image))
                if (xmin <= x <= xmax and ymin <= y <= ymax)
                else infinite_value
            )
    return idx


def enhance(image, algorithm, infinite_value):
    xmin, xmax = min(p[0] for p in image), max(p[0] for p in image)
    ymin, ymax = min(p[1] for p in image), max(p[1] for p in image)

    return set(
        (i, j)
        for i in range(xmin - 1, xmax + 2)
        for j in range(ymin - 1, ymax + 2)
        if algorithm[get_index(image, (i, j), infinite_value, xmin, xmax, ymin, ymax)]
    )


def enhance_for(n, data):
    algorithm, image = data
    for i in range(n):
        infinite_value = i & 1 & algorithm[0]
        image = enhance(image, algorithm, infinite_value)

    return len(image)


@timer
def part1(data):
    return enhance_for(2, data)


@timer
def part2(data):
    return enhance_for(50, data)


@timer
def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
