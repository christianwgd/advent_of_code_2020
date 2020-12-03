# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def find2020():
    # day 1
    with open('numbers.txt', 'r') as numfile:
        numbers = numfile.readlines()
    numbers = [int(x.strip()) for x in numbers]

    for number in numbers:
        for num in numbers:
            for n in numbers:
                sum = n + num + number
                if sum == 2020:
                    print(sum, n, num, number, n * num * number)


def check_passwords():
    # day 2
    with open('passwords.txt', 'r') as password_file:
        lines = password_file.readlines()
    all = valid = invalid = 0
    for line in lines:
        all += 1
        rec = line.split(' ')
        minmax = rec[0].split('-')
        min = int(minmax[0]) - 1
        max = int(minmax[1]) - 1
        char = rec[1][0]
        pw = rec[2].rstrip("\n")
        # count = pw.count(char)
        print('rule:{} check:{} in {}/{} {}'.format(minmax, char, pw[min], pw[max], pw))
        # part 1
        # if count >= int(min) and count <= int(max):
        #     print('valid')
        #     valid += 1
        # else:
        #     print('invalid')
        #     invalid += 1

        if (pw[min] == char and pw[max] != char) or (pw[min] != char and pw[max] == char):
            print('valid')
            valid += 1
        else:
            print('invalid')
            invalid += 1

    print(all, valid, invalid)
    print('valid:', valid)


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
        # print(path)
    return count


def navmap():
    # day 3
    steps = [(1,1), (3,1), (5,1), (7,1), (1,2)]

    with open('map.txt', 'r') as password_file:
    # with open('testmap.txt', 'r') as password_file:
        lines = password_file.readlines()
        # part 1
        # count = nav(lines, 3, 1)
        # print(count)

        # part 2
        product = 1
        for step in steps:
            count = nav(lines, step[0], step[1])
            print('Count:', count)
            product = product * count
        print('Product:', product)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # find2020()
    # check_passwords()
    navmap()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
