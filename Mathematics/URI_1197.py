def math():
    try:
        while True:
            a, b = map(int, input().split())
            print(a * b * 2)

    except EOFError:
        exit()


if __name__ == '__main__':
    math()
