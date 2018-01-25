def math():
    a = int(input())

    if 1 <= a <= 1000:
        for i in range(a, 0, -1)[::-1]:
            if i % 2 == 1:
                print(i)


if __name__ == '__main__':
    math()
