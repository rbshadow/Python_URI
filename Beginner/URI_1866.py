def math():
    test_case = int(input())

    for i in range(test_case):
        i_put = int(input())

        if i_put % 2 == 1:
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    math()
