def find2020():
    # day 1
    with open('day1/numbers.txt', 'r') as numfile:
        numbers = numfile.readlines()
    numbers = [int(x.strip()) for x in numbers]

    for number in numbers:
        for num in numbers:
            for n in numbers:
                sum = n + num + number
                if sum == 2020:
                    print(sum, n, num, number, n * num * number)