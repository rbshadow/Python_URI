def math():
    read = float(input())

    for i in range(100):
        print('N[' + str(i) + '] =', read.__format__('.4f'))
        read /= 2


if __name__ == '__main__':
    math()
