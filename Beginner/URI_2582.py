def math():
    test_case = int(input())

    for i in range(test_case):
        a, b = map(int, input().split())

        res = a + b

        if res == 0:
            print('PROXYCITY')
        elif res == 1:
            print('P.Y.N.G.')
        elif res == 2:
            print('DNSUEY!')
        elif res == 3:
            print('SERVERS')
        elif res == 4:
            print('HOST!')
        elif res == 5:
            print('CRIPTONIZE')
        elif res == 6:
            print('OFFLINE DAY')
        elif res == 7:
            print('SALT')
        elif res == 8:
            print('ANSWER!')
        elif res == 9:
            print('RAR?')
        elif res == 10:
            print('WIFI ANTENNAS')


if __name__ == '__main__':
    math()
