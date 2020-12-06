def check_passwords():
    # day 2
    with open('day2/passwords.txt', 'r') as password_file:
        lines = password_file.readlines()
    all = valid = invalid = 0
    for line in lines:
        all += 1
        rec = line.split(' ')
        minmax = rec[0].split('-')
        min = int(minmax[0]) - 1
        max = int(minmax[1]) - 1
        char = rec[1][0]
        pw = rec[2].rstrip("\n")
        # count = pw.count(char)
        print('rule:{} check:{} in {}/{} {}'.format(minmax, char, pw[min], pw[max], pw))
        # part 1
        # if count >= int(min) and count <= int(max):
        #     print('valid')
        #     valid += 1
        # else:
        #     print('invalid')
        #     invalid += 1

        if (pw[min] == char and pw[max] != char) or (pw[min] != char and pw[max] == char):
            print('valid')
            valid += 1
        else:
            print('invalid')
            invalid += 1

    print(all, valid, invalid)
    print('valid:', valid)