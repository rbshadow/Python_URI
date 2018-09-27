def power():
    test_case = int(input())

    for i in range(test_case):
        base, p_ower = map(int, input().strip().split())

        total = pow(base, p_ower)
        print(len(str(total)))


if __name__ == '__main__':
    power()
