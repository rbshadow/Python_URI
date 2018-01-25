def math():
    a = float(input()).__format__('.2f')

    if 0.00 <= float(a) <= 2000.00:
        print('Isento')
    elif float(a) >= 2000.01:
        a = (float(a) - 2000.00).__format__('.2f')

        if float(a) <= 1000.00:
            a = (float(a) * .08).__format__('.2f')
            print('R$', a)

        if 1000.01 <= float(a) <= 2500.00:
            a = float(a) - 1000
            a = (1000 * .08 + (float(a) * .18)).__format__('.2f')
            print('R$', a)

        if float(a) > 2500.00:
            a = float(a) - 2500
            a = (1000 * .08 + 1500 * .18 + (float(a) * .28)).__format__('.2f')
            print('R$', a)


if __name__ == '__main__':
    math()
