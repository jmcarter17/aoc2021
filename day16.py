from math import prod
from utils import timer


def hex_to_bin(hexstr):
    return "".join(
        ["0" * (4 - len(bin(int(x, 16))[2:])) + bin(int(x, 16))[2:] for x in hexstr]
    )


@timer
def get_data():
    with open("inputs/day16.txt") as f:
        return hex_to_bin(f.read().strip())


def parse_header(header):
    return {"ver": int(header[:3], 2), "tid": int(header[3:], 2), "sub": []}


def parse_literal_value(raw):
    bits = ""
    pos = 0
    while raw[pos] == "1":
        bits += raw[pos + 1 : pos + 5]
        pos += 5
    bits += raw[pos + 1 : pos + 5]
    pos += 5

    return int(bits, 2), pos


def parse_operator_len(raw):
    subtrees = []
    pos = 15
    sp_len = int(raw[:pos], 2)
    while pos < 15 + sp_len:
        tree, pos = parse_package(raw, pos)
        subtrees.append(tree)

    return subtrees, pos


def parse_operator_num(raw):
    subtrees = []
    pos = 11
    num_sp = int(raw[:pos], 2)
    for _ in range(num_sp):
        tree, pos = parse_package(raw, pos)
        subtrees.append(tree)

    return subtrees, pos


def parse_operator(raw):
    if raw[0] == "0":
        subtrees, pos = parse_operator_len(raw[1:])
    else:
        subtrees, pos = parse_operator_num(raw[1:])

    return subtrees, pos + 1


def parse_package(raw, idx):
    tree = parse_header(raw[idx : idx + 6])
    idx += 6

    if tree["tid"] == 4:
        tree["val"], pos = parse_literal_value(raw[idx:])
        idx += pos
    else:
        tree["sub"], pos = parse_operator(raw[idx:])
        idx += pos
        tree["val"] = eval_tree(tree)

    return tree, idx


def sum_versions(tree):
    return tree["ver"] + sum((sum_versions(t) for t in tree["sub"]), 0)


def eval_tree(tree):
    if "val" in tree:
        return tree["val"]
    subtrees = (eval_tree(x) for x in tree["sub"])
    if tree["tid"] == 0:
        return sum(subtrees)
    if tree["tid"] == 1:
        return prod(subtrees)
    if tree["tid"] == 2:
        return min(subtrees)
    if tree["tid"] == 3:
        return max(subtrees)
    if tree["tid"] == 5:
        c1, c2 = subtrees
        return c1 > c2
    if tree["tid"] == 6:
        c1, c2 = subtrees
        return c1 < c2
    if tree["tid"] == 7:
        c1, c2 = subtrees
        return c1 == c2


@timer
def part1(tree):
    return sum_versions(tree)


@timer
def part2(tree):
    return eval_tree(tree)


@timer
def main():
    data = get_data()
    tree, _ = parse_package(data, 0)
    print(part1(tree))
    print(part2(tree))


if __name__ == "__main__":
    main()
