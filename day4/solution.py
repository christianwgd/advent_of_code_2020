def check_passport(p):
    if 'byr' not in p:
        return False
    if not p['byr'].isnumeric():
        return False
    if len(p['byr']) != 4 or int(p['byr']) < 1920 or int(p['byr']) > 2002:
        return False

    if 'iyr' not in p:
        return False
    if not p['iyr'].isnumeric():
        return False
    if len(p['iyr']) != 4 or int(p['iyr']) < 2010 or int(p['iyr']) > 2020:
        return False

    if 'eyr' not in p:
        return False
    if not p['eyr'].isnumeric():
        return False
    if len(p['eyr']) != 4 or int(p['eyr']) < 2020 or int(p['eyr']) > 2030:
        return False

    if 'hgt' not in p:
        return False
    height = p['hgt'][:-2]
    unit = p['hgt'][-2:]
    if not height.isnumeric():
        return False
    # print(height, unit)
    if unit == 'cm':
        if int(height) < 150 or int(height) > 193:
            return False
    elif unit == 'in':
        if int(height) < 59 or int(height) > 76:
            return False
    else:
        return False

    if 'hcl' not in p:
        return False
    if not re.search(r'^#([0-9a-f]{6})$', p['hcl']):
        print(p['hcl'], False)
        return False
    else:
        print(p['hcl'], True)

    if 'ecl' not in p:
        return False
    if p['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if 'pid' not in p:
        return False
    if not re.search(r'^[0-9]{9}$', p['pid']):
        # print(p['pid'], False)
        return False
    else:
        pass
        # print(p['pid'], True)

    return True


def passport_check():
    # day 4
    with open('day4/passports.txt', 'r') as password_file:
        lines = password_file.readlines()

    # part 1
    # required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passports = []
    passport = {}
    for line in lines:
        if line == '\n':
            passports.append(passport)
            passport = {}
        else:
           for prop in line.split(' '):
               passport[prop.split(':')[0]] = prop.split(':')[1].rstrip("\n")

    valid = 0
    for passport in passports:
        # print(passport)
        # validate passport
        if check_passport(passport):
            valid += 1
    print('Valid:', valid)