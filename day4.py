import numpy as np

from utils import timer


@timer
def get_data():
    data = {}
    with open("inputs/day4.txt") as f:
        data["randoms"] = [float(x) for x in f.readline().strip().split(",")]
        data["boards"] = []
        f.readline()
        board = []
        for x in f:
            if x == "\n":
                data["boards"].append(np.array(board))
                board = []
            else:
                board.append([float(val) for val in x.strip().split()])
        data["boards"].append(np.array(board))

    return data


@timer
def part1(data):
    for num in data["randoms"]:
        for b in data["boards"]:
            idx = np.where(b == num)
            if len(idx[0]):
                b[idx] = np.nan
                if np.all(np.isnan(b[idx[0][0], :])) or np.all(np.isnan(b[:, idx[1][0]])):
                    return int(np.nansum(b) * num)


@timer
def part2(data):
    numboards = len(data["boards"])
    removed = set()
    for num in data["randoms"]:
        for i, b in enumerate(data["boards"]):
            if i not in removed:
                idx = np.where(b == num)
                if len(idx[0]):
                    b[idx] = np.nan
                    if np.all(np.isnan(b[idx[0][0], :])) or np.all(np.isnan(b[:, idx[1][0]])):
                        if len(removed) == numboards - 1:
                            return int(np.nansum(b) * num)
                        else:
                            removed.add(i)


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
