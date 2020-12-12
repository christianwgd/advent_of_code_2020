from copy import deepcopy


def check_radius(map, row, seat, check_val):
    count = 0
    max_y = len(map) - 1
    max_x = len(map[0]) - 1
    min_row = row - 1
    min_seat = seat - 1
    max_row = row + 2
    max_seat = seat + 2
    # print(min_row, max_row, min_seat, max_seat)
    for y in range(min_row, max_row):
        for x in range(min_seat, max_seat):
            # print('check', y, x, map[y][x])
            if y < 0:
                # print(y, x, 'exceeds map to upper')
                continue
            if x < 0:
                # print(y, x, 'exceeds map to left')
                continue
            elif y > max_row or y > max_y:
                # print(y, x, 'exceeds map to bottom')
                continue
            elif x > max_seat or x > max_x:
                # print(y, x, 'exceeds map to right')
                continue
            elif y == row and x == seat:
                # print(y, x, 'self')
                continue
            else:
                # print('check', y, x, check_val, map[y][x], map[y][x] == check_val)
                if map[y][x] == check_val:
                    # print('found', check_val, 'at', y, x)
                    count += 1
    # print('count', count)
    return count


def seating(map):
    new_map = deepcopy(map)
    something_changed = False
    for y in range(len(map)):
        row = map[y]
        for x in range(len(row)):
            # print(y, x)
            if map[y][x] == 'L':
                if check_radius(map, y, x, '#') == 0:
                    something_changed = True
                    new_map[y][x] = '#'
            elif map[y][x] == '#':
                if check_radius(map, y, x, '#') > 3:
                    something_changed = True
                    new_map[y][x] = 'L'
            else:
                pass
    # print(new_map)
    return something_changed, new_map


def get_map():
    with open('day11/seatmap.txt', 'r') as password_file:
        lines = password_file.readlines()

    seatmap = []
    for line in lines:
        row = []
        for c in line.rstrip('\n'):
            row.append(c)
        seatmap.append(row)
    return seatmap


def count_occupied_seats(seatmap):
    count = 0
    for y in range(len(seatmap)):
        row = seatmap[y]
        for x in range(len(row)):
            if seatmap[y][x] == '#':
                count += 1
    return count


def display_seatmap(map):
    for row in map:
        print(row)
    print('-----------')


def part1():
    seatmap = get_map()

    # display_seatmap(seatmap)
    # check_radius(seatmap, 1, 0, '#')
    display_seatmap(seatmap)
    changed = True
    while changed:
        changed, seatmap = seating(seatmap)
        display_seatmap(seatmap)
        print('changed', changed)
    count = count_occupied_seats(seatmap)
    return count


def part2():
    with open('day11/test-seatmap.txt', 'r') as password_file:
        lines = password_file.readlines()
