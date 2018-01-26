def math():
    i_put = int(input())

    for i in range(i_put):
        i = int(input())
        if i < 0 and i % 2 == 1:
            print('ODD NEGATIVE')
        elif i < 0 and i % 2 == 0:
            print('EVEN NEGATIVE')
        elif i == 0:
            print('NULL')
        elif i > 0 and i % 2 == 1:
            print('ODD POSITIVE')
        elif i > 0 and i % 2 == 0:
            print('EVEN POSITIVE')


if __name__ == '__main__':
    math()
