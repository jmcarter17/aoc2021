from utils import timer


@timer
def get_data():
    with open("inputs/day8.txt") as f:
        return [[x.split(" ") for x in val.strip().split(" | ")] for val in f]


@timer
def part1(data):
    return len([None for (_, o) in data for x in o if len(x) in [2, 3, 4, 7]])


def compute_digits(segments):
    segments = sorted((frozenset(x) for x in segments), key=len)
    res = [
        None,
        segments[0],
        None,
        None,
        segments[2],
        None,
        None,
        segments[1],
        segments[9],
        None,
    ]
    for seg in segments[3:6]:
        if seg | res[1] == seg:
            res[3] = seg
        elif seg | (res[4] - res[1]) == seg:
            res[5] = seg
        else:
            res[2] = seg
    for seg in segments[6:9]:
        if seg | res[4] == seg:
            res[9] = seg
        elif seg | (res[4] - res[1]) == seg:
            res[6] = seg
        else:
            res[0] = seg

    return res


@timer
def part2(data):
    acc = 0
    for i, o in data:
        digits = compute_digits(i)
        acc += int("".join(str(digits.index(frozenset(v))) for v in o))
    return acc


@timer
def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
