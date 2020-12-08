def check_for_color(color_rules, color):
    for c in color_rules:
        if c['color'] == color:
            return True


def get_bag_by_name(bags, name):
    bag = next(item for item in bags if item["name"] == name)
    return bag


def find_bags(bag, bags, color):
    print('check bag:', bag)
    found = False
    if check_for_color(bag['rules'], color):
        print('found', bag)
        found = True
    else:
        for rule in bag['rules']:
            if rule['max'] > 0:
                inner_bag = get_bag_by_name(bags, rule['color'])
                found = found or find_bags(inner_bag, bags, color)
            else:
                found = False
    return found


def part1():
    with open('day7/bag_rules.txt', 'r') as password_file:
        lines = password_file.readlines()
    bags = []
    for line in lines:
        rule_str = line.split('contain')
        container_parts = rule_str[0].split(' ')
        container = container_parts[0] + ' ' + container_parts[1]
        rule_txt = rule_str[1].lstrip(' ').split(', ')
        rules = []
        for r in rule_txt:
            rl = r.split(' ')
            if rl[0] == 'no':
                rules.append({'max': 0, 'color': ''})
            else:
                rules.append({'max': int(rl[0]), 'color': rl[1] + ' ' + rl[2]})
        bags.append({'name': container, 'rules': rules})

    for rule in bags:
        print(rule)

    find = 'shiny gold'
    count = 0
    for bag in bags:
        if bag['name'] == find:
            continue
        found = find_bags(bag, bags, find)
        if found:
            count += 1
        print(found)

    return count


def count_bags(bag, bags, count):
    print('check', bag)
    for rule in bags[bag]:
        print('rule', rule)
        if rule['max'] > 0:
            inner_bag = rule['color']
            inner_count = count_bags(inner_bag, bags, count)
            print('inner count', count)
            prd = rule['max'] * inner_count
            print('prd', prd)
            count += prd
        else:
            count += 1
    return count


def part2():
    with open('day7/test_bag_rules.txt', 'r') as password_file:
        lines = password_file.readlines()

    bags = {}
    for line in lines:
        rule_str = line.split('contain')
        container_parts = rule_str[0].split(' ')
        container = container_parts[0] + ' ' + container_parts[1]
        rule_txt = rule_str[1].lstrip(' ').split(', ')
        rules = []
        for r in rule_txt:
            rl = r.split(' ')
            if rl[0] == 'no':
                rules.append({'max': 0, 'color': ''})
            else:
                rules.append({'max': int(rl[0]), 'color': rl[1] + ' ' + rl[2]})
        bags[container] = rules

    print(bags)

    find = 'shiny gold'
    count = count_bags(find, bags, count=0)
    return count
