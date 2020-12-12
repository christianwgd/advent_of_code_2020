def get_content():
    with open('day12/input.txt', 'r') as password_file:
        lines = password_file.readlines()
    return lines


def turn(old_heading, direction, degree):
    deg = degree // 90
    directions = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

    if direction == 'R':
        new_value = directions[old_heading] + deg
        if new_value > 3:
            new_value = new_value - 4
    else:
        new_value = directions[old_heading] - deg
        if new_value < 0:
            new_value = new_value + 4

    for dir, val in directions.items():
        if val == new_value:
            return dir


def part1():
    navinstructions = get_content()
    heading = 'E'
    pos = (0, 0)
    for instr in navinstructions:
        instr = instr.rstrip('\n')
        direction = instr[0]
        value = int(instr.rstrip('\n')[1:])
        print(direction, value)

        if direction == 'N' or (direction == 'F' and heading == 'N'):
            pos = (pos[0], pos[1] + value)
        elif direction == 'S' or (direction == 'F' and heading == 'S'):
            pos = (pos[0], pos[1] - value)
        elif direction == 'E' or (direction == 'F' and heading == 'E'):
            pos = (pos[0] + value, pos[1])
        elif direction == 'W' or (direction == 'F' and heading == 'W'):
            pos = (pos[0] - value, pos[1])
        elif direction == 'L':
            heading = turn(heading, direction, value)
        elif direction == 'R':
            heading = turn(heading, direction, value)
        else:
            pass
        print('pos', pos, 'head', heading)

    return (abs(pos[0]) + abs(pos[1]))


def turn2(direction, value, waypoint):
    if direction == 'R':
        if value == 90:
            new_wp = (waypoint[1] * -1, waypoint[0])
        elif value == 180:
            new_wp = (waypoint[0] * -1, waypoint[1] * -1)
        elif value == 270:
            new_wp = (waypoint[1], waypoint[0] * -1)
    else:
        if value == 90:
            new_wp = (waypoint[1], waypoint[0] * -1)
        elif value == 180:
            new_wp = (waypoint[0] * -1, waypoint[1] * -1)
        elif value == 270:
            new_wp = (waypoint[1] * -1, waypoint[0])
    return new_wp


def part2():
    navinstructions = get_content()
    pos = (0, 0)
    waypoint = (1, 10)
    for instr in navinstructions:
        instr = instr.rstrip('\n')
        direction = instr[0]
        value = int(instr.rstrip('\n')[1:])
        print('instruction', direction, value)

        if direction == 'N':
            waypoint = (waypoint[0]+value, waypoint[1])
        elif direction == 'S':
            waypoint = (waypoint[0]-value, waypoint[1])
        elif direction == 'E':
            waypoint = (waypoint[0], waypoint[1]+value)
        elif direction == 'W':
            waypoint = (waypoint[0], waypoint[1]-value)
        elif direction == 'L':
            waypoint = turn2(direction, value, waypoint)
        elif direction == 'R':
            waypoint = turn2(direction, value, waypoint)
        elif direction == 'F':
            pos0 = pos[0] + (waypoint[0] * value)
            pos1 = pos[1] + (waypoint[1] * value)
            pos = (pos0, pos1)
        else:
            pass
        print('pos', pos, 'waypoint', waypoint)

    return(abs(pos[0]) + abs(pos[1]))