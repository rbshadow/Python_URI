def math():
    x, y = map(int, input().split())

    if x > y:
        print('Decrescente')
        math()
    elif x < y:
        print('Crescente')
        math()
    elif x == y:
        exit()


if __name__ == '__main__':
    math()
