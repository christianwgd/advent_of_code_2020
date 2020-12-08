def execute(program, substitute):
    pos = 0
    acc = 0
    loop = False
    while True:
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
            'changed': False
        })

    return execute(program)


def change_next_instr(program, frm, to):
    print('change')
    for step in program:
        if step['instr'] == frm and not step['changed']:
            step['instr'] = to
            step['changed'] = True
    return False


def part2():
    with open('day8/test-input.txt', 'r') as password_file:
        lines = password_file.readlines()

    program = []
    for line in lines:
        instruction = line.rstrip('\n').split(' ')
        program.append({
            'instr': instruction[0],
            'op': int(instruction[1]),
            'exec': False,
            'changed': False
        })

    loop = True
    change = True
    while loop and change:
        change = change_next_instr(program, 'nop', 'jmp')
        print(program)
        acc, loop = execute(program)
        print('loop', loop, 'change', change)

    return acc
