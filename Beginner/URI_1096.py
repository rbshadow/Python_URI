def math():

    for i in range(1, 10, 2):
        j = 7
        for p in range(3):
            print('I=' + str(i), 'J=' + str(j))
            j -= 1


if __name__ == '__main__':
    math()
