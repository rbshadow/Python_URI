def math():
    a, b = map(int, input().split())

    if 1 <= a <= 13:
        if 1 <= b <= 13:
            if a > b:
                print(a)
            elif a < b:
                print(b)
            elif a == b:
                print(a)


if __name__ == '__main__':
    math()
