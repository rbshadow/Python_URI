import math


def ok():
    try:
        while True:
            i_put = int(input())
            print(int(math.log2(i_put)))

    except EOFError:
        exit()


if __name__ == '__main__':
    ok()
