def math():
    while True:
        a, b = map(int, input().split())

        if a == b == 0:
            break
        else:
            print(a + b)


if __name__ == '__main__':
    math()
