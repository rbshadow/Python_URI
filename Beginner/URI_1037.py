def math():
    a = float(input())

    if 0 <= a <= 100:
        if 0 <= a <= 25.00:
            print('Intervalo [0,25]')
        if 25.01 <= a <= 50.00:
            print('Intervalo (25,50]')
        if 50.01 <= a <= 75.00:
            print('Intervalo (50,75]')
        if 75.01 <= a <= 100.00:
            print('Intervalo (75,100]')
    else:
        print('Fora de intervalo')


if __name__ == '__main__':
    math()
