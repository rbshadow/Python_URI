def math():
    try:
        while True:
            test_case = int(input())

            for i in range(test_case):
                i_put = input()
                count_space = i_put.count(' ')
                count_dot = i_put.count('.')

                if count_space == 0:
                    if count_dot == 1:
                        print('a')
                    elif count_dot == 2:
                        print('b')
                    elif count_dot == 3:
                        print('c')

                elif count_space == 1:
                    if count_dot == 2:
                        print('d')
                    elif count_dot == 4:
                        print('e')
                    elif count_dot == 6:
                        print('f')

                elif count_space == 2:
                    if count_dot == 3:
                        print('g')
                    elif count_dot == 6:
                        print('h')
                    elif count_dot == 9:
                        print('i')

                elif count_space == 3:
                    if count_dot == 4:
                        print('j')
                    elif count_dot == 8:
                        print('k')
                    elif count_dot == 12:
                        print('l')

                elif count_space == 4:
                    if count_dot == 5:
                        print('m')
                    elif count_dot == 10:
                        print('n')
                    elif count_dot == 15:
                        print('o')

                elif count_space == 5:
                    if count_dot == 6:
                        print('p')
                    elif count_dot == 12:
                        print('q')
                    elif count_dot == 18:
                        print('r')

                elif count_space == 6:
                    if count_dot == 7:
                        print('s')
                    elif count_dot == 14:
                        print('t')
                    elif count_dot == 21:
                        print('u')

                elif count_space == 7:
                    if count_dot == 8:
                        print('v')
                    elif count_dot == 16:
                        print('w')
                    elif count_dot == 24:
                        print('x')

                elif count_space == 8:
                    if count_dot == 9:
                        print('y')
                    elif count_dot == 18:
                        print('z')
    except EOFError:
        exit()


if __name__ == '__main__':
    math()
