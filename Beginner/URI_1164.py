def math():
    test_case = int(input())

    for i in range(test_case):
        read = int(input())
        count = 0
        for j in range(1, read):
            if read % j == 0:
                count += j

        if count == read:
            print(read, 'eh perfeito')
        else:
            print(read, 'nao eh perfeito')


if __name__ == '__main__':
    math()
