def math():
    while True:
        read_x = int(input())

        if read_x != 0:
            for i in range(1, read_x+1):
                if i == read_x:
                    print(i, end='')
                else:
                    print(i, end=' ')
        else:
            break
        print()


if __name__ == '__main__':
    math()
