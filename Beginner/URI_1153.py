def math():
    read_x = int(input())

    result = 0
    for i in range(1, read_x+1):
        for j in range(1, i):
            i *= j
            result = i
    print(result)


if __name__ == '__main__':
    math()
