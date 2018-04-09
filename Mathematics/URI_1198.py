def math():
    try:
        while True:
            a, b = map(int, input().split())

            if a > b:
                print(a - b)
            else:
                print(b - a)

    except EOFError:
        exit()


if __name__ == '__main__':
    math()
