def math():
    test_case = int(input())

    for i in range(test_case):
        i_put = input()

        count = len(i_put)
        res = (count/100).__format__('.2f')

        print(res)


if __name__ == '__main__':
    math()
