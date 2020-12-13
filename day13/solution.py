def get_content():
    with open('day13/test-input.txt', 'r') as password_file:
        lines = password_file.readlines()
    return lines


def part1():
    content = get_content()
    earliest = int(content[0].rstrip('\n'))
    busses = content[1].split(',')

    results = []

    for bus in busses:
        if bus != 'x':
            found = False
            depart = earliest
            while not found:
                result = depart % int(bus)
                if result == 0:
                    found = True
                    results.append({'depart': depart, 'bus': int(bus)})
                else:
                    depart += 1

    min = None
    for r in results:
        val = r['depart']
        if min is None:
            min = val
        else:
            if val < min:
                min = val
                result = r
    print('--->',result)
    wait = result['depart'] - earliest
    return wait * result['bus']

def part2():
    content = get_content()
    busses = content[1].split(',')

    bus_departs = []
    for i in range(0, len(busses)):
        if busses[i] != 'x':
            bus_departs.append((i, int(busses[i])))
    print(bus_departs)

    t = 0
    time = bus_departs[0][1]
    departs = []
    departs.append(bus_departs[0][1])
    end = False
    while not end:
        t += time
        for bus in bus_departs:
            cont = True
            print(bus[0], bus[1])
            # print(t, bus[0], (t + bus[0]) % bus[1])
            if ((t + bus[0]) % bus[1]) != 0:
                break
            else:
                if not bus[1] in departs:
                    time = time * bus[1]
                    departs.append(bus[1])
                cont = False
        # print(t)
        if not cont:
            end = True
    print(t)
