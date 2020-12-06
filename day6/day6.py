def solve():
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
