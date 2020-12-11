import itertools


def part1():
    with open('day10/test_input.txt', 'r') as password_file:
        lines = password_file.readlines()

    numbers = []
    numbers.append(0)
    for line in lines:
        numbers.append(int(line.rstrip('\n')))

    numbers = sorted(numbers)
    rating = 0
    max_rating = numbers[len(numbers)-1] + 3
    numbers.append(max_rating)
    one_jolt = 0
    three_jolt = 0
    print('min/max', rating, max_rating)
    for n in numbers:
        valid_ratings = list(range(n+1,n+4))
        for v in valid_ratings:
            if v in numbers:
                diff = v - n
                if diff == 1:
                    one_jolt += 1
                    print('adapter', n, 'joltage', v, 'difference', diff)
                    break
                elif diff == 3:
                    three_jolt += 1
                    print('adapter', n, 'joltage', v, 'difference', diff)
                    break
                else:
                    print('not valid')

    print(one_jolt, three_jolt)
    return one_jolt * three_jolt


def is_valid(numbers, max_rating):
    print(numbers)
    numbers.insert(0, 0)
    numbers.append(max_rating)
    v = None
    for n in numbers:
        if v is not None:
            diff = n - v
            if diff > 3:
                return False
        v = n
    return True


def part2():
    with open('day10/input.txt', 'r') as password_file:
        lines = password_file.readlines()

    numbers = []

    for line in lines:
        numbers.append(int(line.rstrip('\n')))

    numbers = sorted(numbers)
    max_rating = numbers[len(numbers)-1] + 3

    before = 0
    joltages = []
    for n in numbers:
        joltages.append(n - before)
        before = n
    joltages.append(3)

    successive_one_joltages = []
    last = len(joltages) - 1
    streak = 0
    for i, jolt in enumerate(joltages):
        if jolt == 1:
            streak += 1
        else:
            successive_one_joltages.append(streak)
            streak = 0
        if i == last:
            successive_one_joltages.append(streak)

    result = 1
    for s in successive_one_joltages:
        if s == 2:
            result = result * 2
        elif s == 3:
            result = result * 4
        elif s == 4:
            result = result * 7
        elif s == 5:
            result = result * 13
        else:
            pass

    print(result)




    # count = 0
    # for x in range(1, len(numbers)):
    #     data = itertools.combinations(set(numbers), x)
    #     for numb in list(data):
    #         print(numb)
    #     #     if is_valid(list(numb), max_rating):
    #     #         print('valid', list(numb))
    #     #         count += 1
    # #
    # print(count+1)
    return 0
