def math():
    test_case = int(input())

    for i in range(test_case):
        a, b = map(int, input().split())
        print(int((a * b) / 2), 'cm2')


if __name__ == '__main__':
    math()
