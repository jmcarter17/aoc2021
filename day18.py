from functools import reduce
from itertools import permutations

from utils import timer
import json


class Pair:
    def __init__(self, a, b):
        if isinstance(a, list):
            self.fst = Pair(*a)
        else:
            self.fst = a
        if isinstance(b, list):
            self.snd = Pair(*b)
        else:
            self.snd = b

    def __iter__(self):
        return iter((self.fst, self.snd))

    def __repr__(self):
        return f"Pair({self.fst}, {self.snd})"


@timer
def get_data():
    with open("inputs/day18.txt") as f:
        return [Pair(*json.loads(row.strip())) for row in f]


def add_left(n, m):
    if isinstance(n, Pair):
        a, b = n.fst, n.snd
        return Pair(add_left(a, m), b)
    else:
        return n + m


def add_right(n, m):
    if isinstance(n, Pair):
        a, b = n.fst, n.snd
        return Pair(a, add_right(b, m))
    else:
        return n + m


def explode(num, level=0):
    if isinstance(num, Pair):
        l, r = num.fst, num.snd
        if level >= 4:
            return 0, True, l, r
        else:
            l, reduced, lval, rval = explode(l, level + 1)
            if reduced:
                if rval != 0:
                    r = add_left(r, rval)
                    rval = 0
            else:
                r, reduced, lval, rval = explode(r, level + 1)
                if reduced:
                    if lval != 0:
                        l = add_right(l, lval)
                        lval = 0
            if reduced:
                return Pair(l, r), True, lval, rval

    return num, False, 0, 0


def split(num):
    if isinstance(num, int):
        if num >= 10:
            a = num // 2
            return Pair(a, num - a), True
    else:
        l, r = num
        l, reduced = split(l)
        if not reduced:
            r, reduced = split(r)
        if reduced:
            return Pair(l, r), True
    return num, False


def reduce_num(num):
    reduced = True
    while reduced:
        num, reduced, *_ = explode(num)
        if not reduced:
            num, reduced = split(num)

    return num


def add_reduce(num1, num2):
    new_num = Pair(num1, num2)
    while new_num:
        step = reduce_num(new_num)
        if step == new_num:
            return new_num
        new_num = step


def magnitude(num):
    if isinstance(num, Pair):
        return 3 * magnitude(num.fst) + 2 * magnitude(num.snd)
    else:
        return num


@timer
def part1(data):
    final_num = reduce(add_reduce, data)
    return magnitude(final_num)


@timer
def part2(data):
    return max(magnitude(add_reduce(x, y)) for x, y in permutations(data, 2))


@timer
def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
