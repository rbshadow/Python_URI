def math():
    try:
        while True:
            test_case = int(input())
            final = 0
            multiply = 0
            dividor = 0

            for i in range(test_case):
                n, c = map(int, input().split())
                multiply += (n * c)
                dividor += c
                final = (multiply / (dividor * 100)).__format__('.4f')

            print(final)
    except EOFError:
        exit()


if __name__ == '__main__':
    math()
