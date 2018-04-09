def math():
    try:
        while True:
            i_put = int(input())

            if i_put == 0:
                print('vai ter copa!')
            else:
                print('vai ter duas!')

    except EOFError:
        exit()


if __name__ == '__main__':
    math()
