import itertools
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
            program[adr] = get_masked_value(mask, val_str)

    sum = 0
    for key in program:
        sum += program[key]
    return sum


def bin_decode(str):
    result_list = []
    count = str.count('X')
    repl = list(itertools.product(['0', '1'], repeat=count))
    for r in repl:
        res = str
        for b in r:
            res = res.replace('X', b, 1)
        result_list.append(res)
    return result_list



def part2():
    content = get_content()

    prog = []
    for line in content:
        if line.startswith('mask'):
            mask = line.rstrip('\n').split('=')[1].strip(' ')
        else:
            mem = line.rstrip('\n')
            mem_parts = mem.split('=')
            val_str = mem_parts[1].strip(' ')
            new_str = ''
            adr = re.search(r'\d+', mem_parts[0]).group()
            bin_str = str(bin(int(adr)))[2:].zfill(36)
            for i in range(len(bin_str)):
                if mask[i] == '0':
                    new_str += bin_str[i]
                elif mask[i] == '1':
                    new_str += '1'
                else:
                    new_str += mask[i]
            prog.append((new_str, val_str))

    print(prog)

    program = {}
    for bin_str, val_str in prog:
        print('-->', bin_str, val_str)
        prog_list = bin_decode(bin_str)
        for step in prog_list:
            program[step] = val_str

    print(program)

    sum = 0
    for key in program:
        sum += int(program[key])
    return sum