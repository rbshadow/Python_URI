def math():
    while True:
        i_put = int(input())

        if i_put == 0:
            break
        else:
            for i in range(1, i_put+1):
                for j in range(1, i_put+1):
                    print(i, end=' ')
                    j += 1
                print()


if __name__ == '__main__':
    math()
