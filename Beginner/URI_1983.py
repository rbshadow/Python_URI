def math():
    test_case = int(input())
    num = []
    large = []

    for i in range(test_case):
        i_put = input().strip().split()
        num.append(int(i_put[0]))
        large.append(float(i_put[1]))

    maximum = max(large)
    position = large.index(maximum)

    if maximum >= 8:
        print(num[position])
    else:
        print('Minimum note not reached')


if __name__ == '__main__':
    math()
