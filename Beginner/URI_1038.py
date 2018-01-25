def math():
    x, y = map(int, input().split())

    one = 4.00
    two = 4.50
    three = 5.00
    four = 2.00
    five = 1.50

    if 1 <= x <= 5:
        if x == 1:
            result = (one * y).__format__('.2f')
        elif x == 2:
            result = (two * y).__format__('.2f')
        elif x == 3:
            result = (three * y).__format__('.2f')
        elif x == 4:
            result = (four * y).__format__('.2f')
        elif x == 5:
            result = (five * y).__format__('.2f')
        print('Total: R$', result)


if __name__ == '__main__':
    math()
