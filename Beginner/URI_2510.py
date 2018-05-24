def math():
    test_case = int(input())

    for i in range(test_case):
        i_put = input()

        if 0 < len(i_put) <= 25:
            print('Y')
        else:
            print('N')


if __name__ == '__main__':
    math()
