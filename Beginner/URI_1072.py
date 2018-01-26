def math():
    test_case = int(input())

    in_count = 0
    out_count = 0

    for i in range(test_case):
        i = int(input())
        if i in range(10, 21):
            in_count = in_count + 1
        else:
            out_count = out_count + 1

    print(in_count, 'in')
    print(out_count, 'out')


if __name__ == '__main__':
    math()
