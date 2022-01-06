from utils import timer


@timer
def get_data():
    with open("inputs/day25.txt") as f:
        return [list(row.strip()) for row in f]


def step_east_row(row):
    length = len(row)
    new_row = row[:]
    for i in range(length):
        if row[i] == ">" and row[(i + 1) % length] == ".":
            new_row[i] = "."
            new_row[(i + 1) % length] = ">"

    return new_row


def step_east(data):
    new_data = [step_east_row(row) for row in data]
    return new_data


def step_south_col(col):
    length = len(col)
    new_col = list(col)
    for i in range(length):
        if col[i] == "v" and col[(i + 1) % length] == ".":
            new_col[i] = "."
            new_col[(i + 1) % length] = "v"

    return new_col


def step_south(data):
    new_data = [step_south_col(col) for col in list(zip(*data))]
    return [list(x) for x in zip(*new_data)]


def step(data):
    data = step_east(data)
    data = step_south(data)

    return data


@timer
def part1(data):
    new_data = step(data)
    count = 1

    while new_data != data:
        data = new_data
        new_data = step(data)
        count += 1

    return count


@timer
def main():
    data = get_data()
    print(part1(data))


if __name__ == "__main__":
    main()
