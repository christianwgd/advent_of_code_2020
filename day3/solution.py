def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])


def nav(lines, right, down):
    count = 0
    x = right
    y = down
    while y < len(lines):
        line = lines[y].rstrip("\n")

        while x >= len(line):
            line += lines[y].rstrip("\n")

        if line[x] == '.':
            path = replace_str_index(line, x, 'O')
        else:
            path = replace_str_index(line, x, 'X')
            count += 1
        y += down
        x += right
        print(path)
    return count


def part1():
    # with open('day3/map.txt', 'r') as password_file:
    with open('day3/testmap.txt', 'r') as password_file:
        lines = password_file.readlines()
        # part 1
        count = nav(lines, 3, 1)
        print(count)


def part2():
    steps = [(1,1), (3,1), (5,1), (7,1), (1,2)]

    # with open('day3/map.txt', 'r') as password_file:
    with open('day3/testmap.txt', 'r') as password_file:
        lines = password_file.readlines()
        product = 1
        for step in steps:
            count = nav(lines, step[0], step[1])
            print('Count:', count)
            product = product * count
        print('Product:', product)