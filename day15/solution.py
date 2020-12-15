from datetime import datetime


def part1():
    numbers = {14: [1], 1: [2], 17: [3], 0: [4], 3: [5]}
    spoken = 20
    turn = 6

    while turn <= 2020:
        # print(turn, numbers, spoken)
        if spoken in numbers:
            numbers[spoken].append(turn)  # add turn number
            times_spoken = len(numbers[spoken])
            # print('history', numbers[spoken])
            prev_turn = numbers[spoken][-1]
            if times_spoken > 1:
                prev_prev = numbers[spoken][-2]
            else:
                prev_prev = 0
            # print(number, 'spoken', times_spoken, 'times')
            # print('next', prev_turn, '-', prev_prev, '=',  prev_turn - prev_prev)
            next = prev_turn - prev_prev

        else:
            numbers[spoken] = []
            numbers[spoken].append(turn)
            next = 0
        print('turn', turn, 'spoken', spoken, '---> next', next)
        turn += 1
        result = spoken
        spoken = next

    return result

def part2():
    # numbers = {0: [1], 3: [2]}
    # spoken = 6
    # turn = 3
    starttime = datetime.now()

    numbers = {14: [1], 1: [2], 17: [3], 0: [4], 3: [5]}
    spoken = 20
    turn = 6

    while turn <= 30000000:
        # print(turn, numbers, spoken)
        if spoken in numbers:
            numbers[spoken].append(turn)  # add turn number
            times_spoken = len(numbers[spoken])
            # print('history', numbers[spoken])
            prev_turn = numbers[spoken][-1]
            if times_spoken > 1:
                prev_prev = numbers[spoken][-2]
            else:
                prev_prev = 0
            # print(number, 'spoken', times_spoken, 'times')
            # print('next', prev_turn, '-', prev_prev, '=',  prev_turn - prev_prev)
            next = prev_turn - prev_prev

        else:
            numbers[spoken] = []
            numbers[spoken].append(turn)
            next = 0
        # print('turn', turn, 'spoken', spoken, '---> next', next)
        turn += 1
        result = spoken
        spoken = next

    print(datetime.now() - starttime)
    return result