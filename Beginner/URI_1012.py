def math():
    a, b, c = input().split()
    a, b, c = float(a), float(b), float(c)

    pi = 3.14159
    triangle = (.5 * a * c).__format__('.3f')
    circular = (pi * (c**2)).__format__('.3f')
    trapezium = (((a + b) / 2) * c).__format__('.3f')
    area = (b**2).__format__('.3f')
    rectangle = (a * b).__format__('.3f')

    print('TRIANGULO:', triangle +
          '\nCIRCULO:', circular +
          '\nTRAPEZIO:', trapezium +
          '\nQUADRADO:', area +
          '\nRETANGULO:', rectangle
          )


if __name__ == '__main__':
    math()
