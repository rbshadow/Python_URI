def math():
    try:
        while True:
            time = input().split(':')
            time = list(map(int, time))

            if 7 <= time[0] <= 9:
                hrs = time[0] * 60 + time[1] - 420
                print('Atraso maximo:', hrs)
            else:
                print('Atraso maximo: 0')
    except EOFError:
        exit()


if __name__ == '__main__':
    math()
