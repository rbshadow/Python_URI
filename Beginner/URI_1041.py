def math():
    x, y = map(float, input().split())

    if x == y == 0.0:
        print('Origem')
    elif x >= 0.1 and y >= 0.1:
        print('Q1')
    elif x < 0.0 and y >= 0.1:
        print('Q2')
    elif x < 0.0 and y < 0.0:
        print('Q3')
    elif x > 0.0 > y:
        print('Q4')
    elif x == 0.0 and y != 0:
        print('Eixo Y')
    elif y == 0.0 and x != 0:
        print('Eixo X')


if __name__ == '__main__':
    math()
