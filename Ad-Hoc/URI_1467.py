def math():
    try:
        while True:
            a, b, c = map(int, input().split())

            if a == 0 and b == 1 and c == 1:
                print('A')
            elif a == 1 and b == 0 and c == 0:
                print('A')

            elif a == 0 and b == 1 and c == 0:
                print('B')
            elif a == 1 and b == 0 and c == 1:
                print('B')

            elif a == 0 and b == 0 and c == 1:
                print('C')
            elif a == 1 and b == 1 and c == 0:
                print('C')

            elif a == 0 and b == 0 and c == 0:
                print('*')
            elif a == 1 and b == 1 and c == 1:
                print('*')
            else:
                print('Else')

    except EOFError:
        exit()


if __name__ == '__main__':
    math()
