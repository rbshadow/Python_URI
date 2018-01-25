def math():
    a, b, c = map(float, input().split())

    if ((b + c) > a) and ((a + c) > b) and ((a + b) > c):
        perimeter = (a + b + c)
        print('Perimetro =', perimeter)
    else:
        area = (((a + b) / 2) * c).__format__('.1f')
        print('Area =', area)


if __name__ == '__main__':
    math()

