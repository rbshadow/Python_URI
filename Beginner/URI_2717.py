def math():
    time = int(input())
    a, b = map(int, input().split())
    res = a + b

    if res <= time:
        print('Farei hoje!')
    else:
        print('Deixa para amanha!')


if __name__ == '__main__':
    math()
