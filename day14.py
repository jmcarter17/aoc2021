from collections import Counter
from functools import cache
from utils import timer


@timer
def get_data():
    with open("inputs/day14_test.txt") as f:
        polymer = f.readline().strip()
        f.readline()
        rules = dict(x.strip().split(" -> ") for x in f)

        return polymer, rules


def solve(polymer, rules, num_generations):
    @cache
    def generate(p, generations):
        if generations == 0:
            return Counter(p)

        c = rules[p]
        return (
            generate(p[0] + c, generations - 1)
            + generate(c + p[1], generations - 1)
            - Counter(c)
        )

    counter = Counter()
    for pair in zip(polymer, polymer[1:]):
        counter += generate("".join(pair), num_generations)

    counter -= Counter(polymer[1:-1])
    most_commons = counter.most_common()

    return most_commons[0][1] - most_commons[-1][1]


@timer
def part1(polymer, rules):
    return solve(polymer, rules, 10)


@timer
def part2(polymer, rules):
    return solve(polymer, rules, 40)


@timer
def main():
    polymer, rules = get_data()
    print(part1(polymer, rules))
    print(part2(polymer, rules))


if __name__ == "__main__":
    main()
