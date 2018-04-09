def math():
    while True:
        test_case = int(input())
        mary = 0
        john = 0

        if test_case != 0:
                i_put = input().split()
                lis_t = list(map(int, i_put))
                for i in lis_t:
                    if i == 0:
                        mary += 1
                    else:
                        john += 1
                print('Mary won ' + str(mary) + ' times and John won ' + str(john) + ' times')
        else:
            exit()


if __name__ == '__main__':
    math()
