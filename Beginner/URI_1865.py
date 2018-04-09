def math():
    test_case = int(input())

    for i in range(test_case):
        name, mass = (map(str, input().split()))

        if name == 'Thor':
            print('Y')
        else:
            print('N')


if __name__ == '__main__':
    math()
