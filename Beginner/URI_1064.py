def math():
    res = 0
    pos = 0
    for i in range(6):
        i = input()
        if float(i) > 0.0:
            pos = pos + 1
            res = res + float(i)

    print(str(pos) + ' valores positivos')
    print((res / pos).__format__('.1f'))


if __name__ == '__main__':
    math()
