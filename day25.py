from utils import timer


@timer
def get_data():
    with open("inputs/day25.txt") as f:
        return [row.strip() for row in f]


def replace(string, c):
    old = c + "."
    new = "." + c
    if string[-1] + string[0] == old:
        string = "_" + string[1:-1] + "x"
    string = string.replace(old, new).replace("_", c).replace("x", ".")
    return string


def step(cucumbers):
    step_east = [replace(row, ">") for row in cucumbers]
    return ["".join(x) for x in zip(*(replace("".join(col), "v") for col in zip(*step_east)))]


@timer
def part1(cucumbers):
    count = 0
    while True:
        count += 1
        new_cucumbers = step(cucumbers)
        if new_cucumbers == cucumbers:
            return count
        cucumbers = new_cucumbers


@timer
def main():
    data = get_data()
    print(part1(data))


if __name__ == "__main__":
    main()
