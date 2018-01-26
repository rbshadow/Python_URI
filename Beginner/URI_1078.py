def math():
    i_put = int(input())

    if 1 < i_put < 1000:
        for i in range(1, 11):
            print(i, 'x', i_put, '=', i*i_put)


if __name__ == '__main__':
    math()
