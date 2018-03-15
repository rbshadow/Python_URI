def math():
    test_case = int(input())

    for i in range(test_case):
        number = []

        start, end = map(int, input().split())

        for n in range(start, end+1):
            number.extend(str(n))

        length = len(number)

        for l in range(length):
            print(number[l], end='')

        for l in range(0, length)[::-1]:
            print(number[l], end='')
        print()


if __name__ == '__main__':
    math()
