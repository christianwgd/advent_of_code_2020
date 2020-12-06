def solve_part2():
    with open('day6/answers.txt', 'r') as password_file:
        lines = password_file.readlines()

    groups = []
    group = []
    sum = 0
    for line in lines:
        if line == '\n':
            groups.append(group)
            sum += len(group[0].intersection(*group))
            group = []

        else:
            group.append(set(line.rstrip("\n")))

    return sum


def solve_part1():
    with open('day6/answers.txt', 'r') as password_file:
        lines = password_file.readlines()

    groups = []
    group = []
    product = 0
    for line in lines:
        if line == '\n':
            groups.append(group)
            product = product + len(set(group))
            group = []

        else:
            for x in line.rstrip("\n"):
                group.append(x)

    return product
