import math


def maths():
    a, b, c = input().split()
    a, b, c = float(a), float(b), float(c)

    b_square = (b ** 2) - (4 * a * c)

    if a > 0:
        if b_square > 0:
            result1 = (((-b) + math.sqrt(float(b_square))) / (2 * a)).__format__('.5f')
            result2 = (((-b) - math.sqrt(float(b_square))) / (2 * a)).__format__('.5f')
            print('R1 = ' + str(result1) + '\n' +
                  'R2 = ' + str(result2))
        else:
            print('Impossivel calcular')
    else:
        print('Impossivel calcular')


if __name__ == '__main__':
    maths()
