def check_sum(n):
    factors = n[:25]
    result = n[25]
    for x in factors:
        for y in factors:
            if x + y == result:
                return True
    print(result)
    return False


def part1():
    with open('day9/numbers.txt', 'r') as password_file:
        lines = password_file.readlines()

    numbers = []
    for line in lines:
        numbers.append(int(line.rstrip('\n')))

    found = False
    low = 0
    high = 26
    while not found and high <= len(numbers):
        check = numbers[low:high]

        check_sum(check)

        low += 1
        high += 1


def part2():
    with open('day9/numbers.txt', 'r') as password_file:
        lines = password_file.readlines()

    numbers = []
    for line in lines:
        numbers.append(int(line.rstrip('\n')))

    find = 15353384
    #find = 127
    y = 0
    for x in range(len(numbers)):
        if y >= len(numbers)-1:
            break
        else:
            y = x + 1
        while numbers[y] < find:
            result_list = numbers[x:y+1]
            result = sum(result_list)
            if result == find:
                sorted_result_list = sorted(result_list)
                max = len(sorted_result_list) - 1
                return sorted_result_list[0] + sorted_result_list[max]
            y += 1

