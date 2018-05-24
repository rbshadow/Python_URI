def math():
    test_case = int(input())

    for i in range(test_case):
        string = input().split()

        lis_t1 = string[0] + string[1]
        lis_t2 = string[2] + string[3]

        fnumber, snumber = map(int, input().strip().split())
        sum = fnumber + snumber

        answer = []
        wrong = []

        if 'IMPAR' in lis_t1:
            answer = string[2]
            wrong = string[0]

        elif 'IMPAR' in lis_t2:
            answer = string[0]
            wrong = string[2]

        if sum % 2 == 0:
            print(answer)
        else:
            print(wrong)


if __name__ == '__main__':
    math()
