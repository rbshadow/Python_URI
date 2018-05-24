def math():
    test_case = int(input())

    for i in range(test_case):
        a, b = map(int, input().split())
        res = a + b
        print(res)


if __name__ == '__main__':
    math()
