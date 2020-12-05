# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re


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
        print(path)
    return count


def navmap():
    # day 3
    steps = [(1,1), (3,1), (5,1), (7,1), (1,2)]

    # with open('map.txt', 'r') as password_file:
    with open('testmap.txt', 'r') as password_file:
        lines = password_file.readlines()
        # part 1
        count = nav(lines, 3, 1)
        print(count)

        # part 2
        # product = 1
        # for step in steps:
        #     count = nav(lines, step[0], step[1])
        #     print('Count:', count)
        #     product = product * count
        # print('Product:', product)


def check_passport(p):
    if 'byr' not in p:
        return False
    if not p['byr'].isnumeric():
        return False
    if len(p['byr']) != 4 or int(p['byr']) < 1920 or int(p['byr']) > 2002:
        return False

    if 'iyr' not in p:
        return False
    if not p['iyr'].isnumeric():
        return False
    if len(p['iyr']) != 4 or int(p['iyr']) < 2010 or int(p['iyr']) > 2020:
        return False

    if 'eyr' not in p:
        return False
    if not p['eyr'].isnumeric():
        return False
    if len(p['eyr']) != 4 or int(p['eyr']) < 2020 or int(p['eyr']) > 2030:
        return False

    if 'hgt' not in p:
        return False
    height = p['hgt'][:-2]
    unit = p['hgt'][-2:]
    if not height.isnumeric():
        return False
    # print(height, unit)
    if unit == 'cm':
        if int(height) < 150 or int(height) > 193:
            return False
    elif unit == 'in':
        if int(height) < 59 or int(height) > 76:
            return False
    else:
        return False

    if 'hcl' not in p:
        return False
    if not re.search(r'^#([0-9a-f]{6})$', p['hcl']):
        print(p['hcl'], False)
        return False
    else:
        print(p['hcl'], True)

    if 'ecl' not in p:
        return False
    if p['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if 'pid' not in p:
        return False
    if not re.search(r'^[0-9]{9}$', p['pid']):
        # print(p['pid'], False)
        return False
    else:
        pass
        # print(p['pid'], True)

    return True


def passport_check():
    # day 4
    with open('passports.txt', 'r') as password_file:
        lines = password_file.readlines()

    # part 1
    # required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passports = []
    passport = {}
    for line in lines:
        if line == '\n':
            passports.append(passport)
            passport = {}
        else:
           for prop in line.split(' '):
               passport[prop.split(':')[0]] = prop.split(':')[1].rstrip("\n")

    valid = 0
    for passport in passports:
        # print(passport)
        # validate passport
        if check_passport(passport):
            valid += 1
    print('Valid:', valid)


def get_num(str, max):
    values = (0, max)
    for val in str:
        if values[0] == 0:
            middle = (values[1] + 1) // 2 - 1
        else:
            middle = values[1] - ((values[1] - values[0]) // 2) -1
        if val == 'F' or val == 'L':
            values = (values[0], middle)
        else:
            values = (middle + 1, values[1])
    return values[0]


def find_boardingpass():
    with open('boardingpasses.txt', 'r') as password_file:
        lines = password_file.readlines()
    max = 0
    seats = []
    for line in lines:
        seat = get_num(line[:7], 127)
        col = get_num(line[7:], 7)
        id = seat * 8 + col
        if id > max:
            max = id
        #print(seat, col, id, max)
        seats.append(id)
    #print('max:', max)
    seats = sorted(seats)

    check = 80
    for seat in seats:
        print(seat, check)
        if seat != check:
            break
        check += 1
    print(check)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # find2020()
    # check_passwords()
    # navmap()
    # passport_check()
    find_boardingpass()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
