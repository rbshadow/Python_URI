def math():
    i_put = int(input())

    if 5 < i_put < 2000:
        for i in range(1, i_put+1):
            if i % 2 == 0:
                print(str(i) + '^2 =', i*i)


if __name__ == '__main__':
    math()
