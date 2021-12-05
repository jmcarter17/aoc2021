import numpy as np
from utils import timer


@timer
def get_data():
    data = {}
    with open("inputs/day4_test.txt") as f:
        data["randoms"] = [int(x) for x in f.readline().strip().split(",")]
        data["boards"] = []
        f.readline()
        board = []
        for x in f:
            if x == "\n":
                data["boards"].append(np.array(board))
                board = []
            else:
                board.append([int(val) for val in x.strip().split()])
        data["boards"].append(np.array(board))

    return data


@timer
def part1(data):
    for num in data["randoms"]:
        for b in data["boards"]:
            idx = np.where(b == num)
            if len(idx[0]):
                b[idx] = -1
                if np.all(b[idx[0][0], :] == -1) or np.all(b[:, idx[1][0]] == -1):
                    b[np.where(b == -1)] = 0
                    return np.sum(b) * num


@timer
def part2(data):
    numboards = len(data["boards"])
    removed = []
    for num in data["randoms"]:
        for i, b in enumerate(data["boards"]):
            if i not in removed:
                idx = np.where(b == num)
                if len(idx[0]):
                    b[idx] = -1
                    if np.all(b[idx[0][0], :] == -1) or np.all(b[:, idx[1][0]] == -1):
                        if len(removed) == numboards - 1:
                            b[np.where(b == -1)] = 0
                            return np.sum(b) * num
                        else:
                            removed.append(i)


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
