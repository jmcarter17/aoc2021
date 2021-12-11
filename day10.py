from functools import reduce
from statistics import median
from utils import timer

MATCHING = {"(": ")", "[": "]", "{": "}", "<": ">"}
SYNTAX_ERROR_VALUE = {")": 3, "]": 57, "}": 1197, ">": 25137}
COMPLETION_VALUE = {")": 1, "]": 2, "}": 3, ">": 4}


@timer
def get_data():
    with open("inputs/day10_test.txt") as f:
        return [x.strip() for x in f]


def find_error(x):
    stack = []
    for c in x:
        if c in "([{<":
            stack.append(c)
        elif c in ")]}>":
            prev = stack.pop()
            if c != MATCHING[prev]:
                return c
    return stack


def get_completion_vals(x):
    stack = find_error(x)
    if isinstance(stack, str):
        return

    return (COMPLETION_VALUE[MATCHING[x]] for x in reversed(stack))


def syntax_error(x):
    return SYNTAX_ERROR_VALUE[x] if not isinstance(x, list) else 0


@timer
def part1(data):
    return sum(syntax_error(find_error(x)) for x in data)


@timer
def part2(data):
    acc = []
    for x in data:
        vals = get_completion_vals(x)
        if vals:
            acc.append(reduce(lambda a, y: 5 * a + y, vals, 0))

    return median(acc)


@timer
def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
