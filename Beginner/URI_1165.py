def math():
    test_case = int(input())

    for i in range(test_case):
        read = int(input())
        if read > 1:
            print(prime_number(read))
        else:
            print(read, 'nao eh primo')


def prime_number(x):
    if x >= 2:
        for i in range(2, x):
            if x % i == 0:
                return str(x) + ' nao eh primo'
    return str(x) + ' eh primo'


if __name__ == '__main__':
    math()
