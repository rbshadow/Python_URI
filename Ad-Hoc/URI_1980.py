def math():
    while True:
        i_put = input().strip()
        length = len(i_put)
        res = 0

        if i_put != '0':
            if length == 1:
                print(1)
            else:
                for i in range(1, length+1):
                    for j in range(1, i):
                        i *= j
                        res = i
                print(res)
        else:
            exit()


if __name__ == '__main__':
    math()
