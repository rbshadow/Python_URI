def math():
    test_case = int(input())

    for i in range(test_case):
        i_put = int(input())

        if i_put == 2015:
            print('1 A.C.')
        else:
            if i_put > 2015:
                print((i_put - 2015) + 1, 'A.C.')
            elif i_put < 2015:
                print(2015 - i_put, 'D.C.')


if __name__ == '__main__':
    math()
