def math():
    try:
        while True:
            test_case, i_d = map(int, input().split())
            count = 0
            for i in range(test_case):
                iid, cs = map(int, input().split())

                if iid == i_d and cs == 0:
                    count += 1
            print(count)
    except EOFError:
        exit()


if __name__ == '__main__':
    math()
