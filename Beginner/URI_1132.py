def math():
    x, y = int(input()), int(input())

    count = 0
    if x < y:
        for i in range(x, y+1):
            if i % 13 != 0:
                count += i
        print(count)
    else:
        for i in range(y, x+1):
            if i % 13 != 0:
                count += i
        print(count)


if __name__ == '__main__':
    math()
