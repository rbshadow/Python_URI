def math():
    a, b = map(int, input().split())

    if b % a == 0:
        print('Sao Multiplos')
    elif a % b == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')


if __name__ == '__main__':
    math()
