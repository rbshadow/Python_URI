def math():
    x, y = int(input()), int(input())

    if x < y:
        for i in range(y-1, x, -1)[::-1]:
            if i % 5 == 2:
                print(i)
            if i % 5 == 3:
                print(i)
    elif x > y:
        for i in range(x-1, y, -1)[::-1]:
            if i % 5 == 2:
                print(i)
            if i % 5 == 3:
                print(i)


if __name__ == '__main__':
    math()
