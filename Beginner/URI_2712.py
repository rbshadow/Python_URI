def math():
    test_case = int(input())

    for i in range(test_case):
        i_put = input()

        if len(i_put) == 8:
            if '-' in i_put:
                split = i_put.split('-')
                before_hifen = split[0]
                after_hifen = split[1]

                if len(before_hifen) == 3:
                    if len(after_hifen) == 4:
                        if before_hifen == before_hifen.upper():
                            if after_hifen.endswith('1'):
                                print('MONDAY')
                            elif after_hifen.endswith('2'):
                                print('MONDAY')
                            elif after_hifen.endswith('3'):
                                print('TUESDAY')
                            elif after_hifen.endswith('4'):
                                print('TUESDAY')
                            elif after_hifen.endswith('5'):
                                print('WEDNESDAY')
                            elif after_hifen.endswith('6'):
                                print('WEDNESDAY')
                            elif after_hifen.endswith('7'):
                                print('THURSDAY')
                            elif after_hifen.endswith('8'):
                                print('THURSDAY')
                            elif after_hifen.endswith('9'):
                                print('FRIDAY')
                            elif after_hifen.endswith('0'):
                                print('FRIDAY')
                            else:
                                print('FAILURE')
                        else:
                            print('FAILURE')
                    else:
                        print('FAILURE')
                else:
                    print('FAILURE')
            else:
                print('FAILURE')
        else:
            print('FAILURE')


if __name__ == '__main__':
    math()
