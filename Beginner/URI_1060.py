def math():
    sum = 0
    for i in range(6):
        value = []
        value = input()
        if float(value) > 0.0:
            sum = sum + 1

    print(str(sum) + ' valores positivos')


if __name__ == '__main__':
    math()
