def math():
    try:
        while True:
            i_put = int(input())

            if 1000 <= i_put <= 10000:
                print(i_put - 1)
    except EOFError:
        exit()


if __name__ == '__main__':
    math()
