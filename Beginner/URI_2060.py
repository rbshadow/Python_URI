def math():
    t = int(input())

    count_two = 0
    count_three = 0
    count_four = 0
    count_five = 0

    number = list(map(int, input().strip().split()))

    for i in number:
        if i % 2 == 0:
            count_two += 1
        if i % 3 == 0:
            count_three += 1
        if i % 4 == 0:
            count_four += 1
        if i % 5 == 0:
            count_five += 1

    print(count_two, 'Multiplo(s) de 2')
    print(count_three, 'Multiplo(s) de 3')
    print(count_four, 'Multiplo(s) de 4')
    print(count_five, 'Multiplo(s) de 5')


if __name__ == '__main__':
    math()
