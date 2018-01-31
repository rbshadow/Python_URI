def math():
    x, y = map(int, input().split())

    while True:
        if x > 0 and y > 0:
            print('primeiro')
            math()
        elif x < 0 < y:
            print('segundo')
            math()
        elif x < 0 and y < 0:
            print('terceiro')
            math()
        elif x > 0 > y:
            print('quarto')
            math()
        elif x == 0 or y == 0:
            exit()


if __name__ == '__main__':
    math()
