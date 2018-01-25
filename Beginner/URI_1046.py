def math():
    start, end = map(int, input().split())

    if start > end:
        result = ((24 - start) + end)
        print('O JOGO DUROU ' + str(result) + ' HORA(S)')
    elif start == end:
        print('O JOGO DUROU 24 HORA(S)')
    elif start < end:
        result = end - start
        print('O JOGO DUROU ' + str(result) + ' HORA(S)')


if __name__ == '__main__':
    math()
