def math():
    loop = int(input())
    read_list = []
    count = 0

    for j in range(1000):
        for k in range(loop):
            read_list.append(k)

        print('N[' + str(count) + '] =', read_list[j])
        count += 1


if __name__ == '__main__':
    math()
