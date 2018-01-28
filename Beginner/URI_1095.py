def math():
    i_count = 1
    for j in range(0, 65, 5)[::-1]:
        print('I=' + str(i_count), 'J=' + str(j))
        i_count += 3


if __name__ == '__main__':
    math()
