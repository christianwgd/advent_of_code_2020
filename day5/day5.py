def get_num(str, max):
    # make binary from string
    binstr = str.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1')
    return int(binstr, 2)

def find_boardingpass():
    with open('day5/boardingpasses.txt', 'r') as password_file:
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

