def math():
    test_case = int(input())

    a = 0
    b = 1
    result_list = []

    for i in range(test_case):
        number = int(input())

        for j in range(number+1):
            result_list.append(a)
            a, b = b, a + b

        print('Fib(' + str(number) + ') =', result_list[number])


if __name__ == '__main__':
    math()
