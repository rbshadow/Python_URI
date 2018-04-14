def math():
    test_case = int(input())

    for i in range(test_case):
        count = 0
        name = input()
        degree = float(input())
        lis_t = list(map(float, input().strip().split()))
        maximum = max(lis_t)
        minimum = min(lis_t)

        lis_t.remove(maximum)
        lis_t.remove(minimum)

        for j in lis_t:
            count += j

        result = (count * degree).__format__('.2f')
        print(name, result)


if __name__ == '__main__':
    math()
