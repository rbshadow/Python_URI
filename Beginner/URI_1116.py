def math():
    test_case = int(input())

    for i in range(test_case):
        j, k = map(int, input().split())

        if k == 0:
            print('divisao impossivel')
        else:
            res = (j / k)
            print(res)


if __name__ == '__main__':
    math()
