# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def find2020():
    # day 1
    with open('numbers.txt', 'r') as numfile:
        numbers = numfile.readlines()
    numbers = [int(x.strip()) for x in numbers]

    for number in numbers:
        for num in numbers:
            for n in numbers:
                sum = n + num + number
                if sum == 2020:
                    print(sum, n, num, number, n * num * number)


def check_passwords():
    # day 2
    with open('passwords.txt', 'r') as password_file:
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_passwords()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
