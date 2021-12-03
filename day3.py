def get_data():
    with open("inputs/day3.txt") as f:
        return [x.strip() for x in f]


def part1(data):
    gamma = "".join([str(int(x.count('1') > len(data)//2)) for x in zip(*data)])
    beta = "".join([str(int(x == '0')) for x in gamma])
    return int(gamma, 2) * int(beta, 2)


def get_rating(data, criteria_fn):
    for idx in range(len(data[0])):
        bits = list(zip(*data))[idx]
        criteria = criteria_fn(bits)
        data = [x for x in data if x[idx] == criteria]
        if len(data) == 1:
            return int(data[0], 2)


def get_oxy_rating(data):
    criteria_fn = lambda bits: '0' if bits.count('1') < bits.count('0') else '1'
    return get_rating(data, criteria_fn)


def get_co2_rating(data):
    criteria_fn = lambda bits: '1' if bits.count('1') < bits.count('0') else '0'
    return get_rating(data, criteria_fn)


def part2(data):
    return get_oxy_rating(data[:]) * get_co2_rating(data[:])


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
