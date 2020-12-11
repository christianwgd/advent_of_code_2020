def check_seat(map, row, seat, val):
    if map[row][seat] == val:
        return True
    return False


def check_rule1(map, row, seat):
    max_row = len(map) - 1
    max_seat = len(row) - 1
    # der Sitz links oben
    if row == 0 and seat == 0:
        pass
    # Sitze in der ersten Reihe
    elif row == 0 and seat > 0:
        pass
    # Sitze am linken Rand
    elif row > 0 and seat == 0:
        pass
    # der Sitz rechts unten
    elif row == max_row and seat == max_seat:
        pass
    # Sitze am rechten Rand
    elif row < max_row and seat == max_seat:
        pass
    # Sitze in der letzten Reihe
    elif row == max_row and seat < max_seat:
        pass
    # alle anderen in der Mitte
    else:
        pass

    if seat > 0 and row[seat-1] == 'L' and row[seat+1] == 'L':
        return True
    else:
        return False


def check_rule2(row, x, occ):
    # TODO: Wie in check_rule1 auch diagonal, hinten und vorne prüfen!
    for dist in range(occ):
        print('dist:', dist)
        if row[x+occ] == 'L' or row[x+occ] == '.':
            return False
        if row[x+occ] == 'L' or row[x+occ] == '.':
            return False
    return True


def seating(seatmap):
    something_changed = False
    for y in range(len(seatmap)):
        row = seatmap[y]
        for x in range(len(row)):
            if row[x] == '.':
                pass
            elif row[x] == 'L':
                if check_rule1(row, x):
                    row[x] = '#'
                    something_changed = True
            elif row[x] == '#':
                if check_rule2(row, x, 4):
                    row[x] = 'L'
                    something_changed = True
            else:
                pass
        print(row)
    return something_changed


def part1():
    with open('day11/test-seatmap.txt', 'r') as password_file:
        lines = password_file.readlines()

    seatmap = []
    for line in lines:
        row = []
        for c in line.rstrip('\n'):
            row.append(c)
        seatmap.append(row)

    changed = True
    while changed:
        changed = seating(seatmap)
    # count occupied seats


def part2():
    with open('day11/test-seatmap.txt', 'r') as password_file:
        lines = password_file.readlines()
