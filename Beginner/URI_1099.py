def math():

    test_case = int(input())

    for i in range(test_case):
        up_one, up_two = map(int, input().split())
        count = 0
        if up_one < up_two:
            for f in range(up_one, up_two+1):
                if f % 2 == 1 and (f != up_one and f != up_two):
                    count += f
            print(count)
        elif up_two < up_one:
            for f in range(up_two, up_one+1):
                if f % 2 == 1 and (f != up_one and f != up_two):
                    count += f
            print(count)
        else:
            print(count)


if __name__ == '__main__':
    math()
