def math():
    count = 0
    for i in range(10):
        i = int(input())

        if i <= 0:
            print('X[' + str(count) + '] = 1')
        else:
            print('X[' + str(count) + '] =', i)
        count += 1


if __name__ == '__main__':
    math()
