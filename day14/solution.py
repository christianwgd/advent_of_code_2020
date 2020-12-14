import re


def get_content():
    with open('day14/input.txt', 'r') as password_file:
        lines = password_file.readlines()
    return lines


def get_masked_value(mask, val_str):
    new_bin = ''
    bin_str = str(bin(int(val_str)))[2:].zfill(36)
    for i in range(len(bin_str)):
        if mask[i] == 'X':
            new_bin += bin_str[i]
        else:
            new_bin += mask[i] or bin_str[i]

    # print(mask)
    # print(bin_str)
    # print(new_bin)
    return int(new_bin, 2)


def part1():
    content = get_content()

    program = {}
    for line in content:
        if line.startswith('mask'):
            mask = line.rstrip('\n').split('=')[1].strip(' ')
        else:
            mem = line.rstrip('\n')
            mem_parts = mem.split('=')
            adr = int(re.search(r'\d+', mem_parts[0]).group())
            val_str = mem_parts[1].strip(' ')
            new = get_masked_value(mask, val_str)
            program[adr] = new

    sum = 0
    for key in program:
        sum += program[key]
    return sum

def part2():
    content = get_content()