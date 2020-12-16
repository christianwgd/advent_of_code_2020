def get_content():
    with open('day16/input.txt', 'r') as password_file:
        lines = password_file.readlines()

    rules = {}
    i = 0
    while lines[i] != '\n':
        parts1 = lines[i].rstrip('\n').split(':')
        parts2 = parts1[1].split('or')
        rules[parts1[0]] = []
        for p in parts2:
            parts3 = p.strip().split('-')
            rules[parts1[0]].append((int(parts3[0]), int(parts3[1])))

        i += 1
    i += 2
    myticket = [int(x) for x in lines[i].rstrip('\n').split(',')]
    i += 3
    tickets = []
    for line in lines[i:]:
        ticket = [int(x) for x in line.rstrip('\n').split(',')]
        tickets.append(ticket)
        i += 1
    return rules, myticket, tickets


def check_rule(v, r):
    return v >= r[0][0] and v <= r[0][1] or v >= r[1][0] and v <= r[1][1]


def check_field(field, rules):
    for rule in rules:
        if check_rule(field, rules[rule]):
            return True
    return False


def check_ticket(ticket, rules):
    for field in ticket:
        if not check_field(field, rules):
            return False, field
    return True, 0


def part1():
    rules, myticket, tickets = get_content()
    # print('rules', rules)
    # print('myticket', myticket)
    # print('tickets', tickets)

    rate = 0
    for ticket in tickets:
        valid, field_rate = check_ticket(ticket, rules)
        if valid:
            print(ticket, True)
        else:
            rate += field_rate
            print(ticket, False)
    return rate


def part2():
    rules, myticket, tickets = get_content()
    valid_tickets = []
    for ticket in tickets:
        valid, field_rate = check_ticket(ticket, rules)
        if valid:
            valid_tickets.append(ticket)

    pos = {}
    for rule in rules:
        pos[rule] = []

    for col in range(len(myticket)):
        for rule in rules:
            match_ticket = True
            for ticket in valid_tickets:
                if not check_rule(ticket[col], rules[rule]):
                    match_ticket = False
                    break
            if match_ticket:
                pos[rule].append(col)
    # print(pos)

    fields = []
    for p in pos:
        fields.append((p, pos[p], len(pos[p])))

    sorted_fields = sorted(fields, key=lambda tup: tup[2])
    fields = {}
    r = []
    for f in sorted_fields:
        new = []
        lst = f[1]
        name = f[0]
        for l in lst:
            if l not in r:
                new.append(l)
        if len(new) == 1:
            fields[name] = new[0]
            r.append(new[0])

    result = 1
    for field in fields:
        if field.startswith('departure'):
            result = result * myticket[fields[field]]

    return result