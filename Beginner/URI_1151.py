def math():
    i_put = int(input())

    a = 0
    b = 1

    for i in range(i_put):
        if i == (i_put-1):
            print(a, end='')
        else:
            print(a, end=' ')
        a, b = b, a + b
    print()


if __name__ == '__main__':
    math()
