def math():
    lists = []
    count = 0
    for i in range(20):
        j = int(input())
        lists.append(j)

    for j in range(20)[::-1]:
        print('N[' + str(count) + '] =', lists[j])
        count += 1


if __name__ == '__main__':
    math()
