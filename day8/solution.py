def execute(program):
    pos = 0
    acc = 0
    loop = False
    length = len(program)
    while pos < length:
        if program[pos]['exec']:
            loop = True
            break
        # print(program[pos]['instr'], program[pos]['op'])
        program[pos]['exec'] = True
        if program[pos]['instr'] == 'nop':
            pos += 1
        elif program[pos]['instr'] == 'acc':
            acc += program[pos]['op']
            pos += 1
        elif program[pos]['instr'] == 'jmp':
            pos += program[pos]['op']
        else:
            print('illegal instruction')
        # print('pos', pos, 'acc', acc)
    return acc, loop


def part1():
    with open('day8/test-input.txt', 'r') as password_file:
        lines = password_file.readlines()

    program = []
    for line in lines:
        instruction = line.rstrip('\n').split(' ')
        program.append({
            'instr': instruction[0],
            'op': int(instruction[1]),
            'exec': False,
        })

    return execute(program)


def replace_instruction(program, replace, new, pos):
    count = 0
    step_count = 0
    for step in program:
        if step['instr'] == replace:
            count += 1
            print(count, pos)
            if count == pos:
                step['instr'] = new
                # print('changed', pos, replace, 'from', 'to', new)
                return False
        step_count += 1
        if step_count >= len(program):
            return True


def get_copy(program):
    import copy
    prog_copy = []
    for li in program:
        d2 = copy.deepcopy(li)
        prog_copy.append(d2)
    return prog_copy


def part2():
    with open('day8/input.txt', 'r') as password_file:
        lines = password_file.readlines()

    program = []
    for line in lines:
        instruction = line.rstrip('\n').split(' ')
        program.append({
            'instr': instruction[0],
            'op': int(instruction[1]),
            'exec': False,
        })

    loop = True
    pos = 0
    stop = False
    while not stop and loop:
        pos += 1
        print('prog', program)
        print('------->', pos)
        prog_copy = get_copy(program)
        stop = replace_instruction(prog_copy, 'jmp', 'nop', pos)
        # print(count)
        acc, loop = execute(prog_copy)
        print('copy', prog_copy)
        print('loop', loop, pos)
        print('\n\n')

    return acc
