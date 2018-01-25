def math():
    r = float(input())
    r = r**3
    pi = 3.14159
    result = ((4 / 3) * pi * r).__format__('.3f')

    print('VOLUME =', result)


if __name__ == '__main__':
    math()
