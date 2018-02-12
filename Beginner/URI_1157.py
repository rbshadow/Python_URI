def math():
    read_x = int(input())

    for i in range(1, read_x+1):
        if read_x % i == 0:
            print(i)


if __name__ == '__main__':
    math()
