def math():
    try:
        while True:
            string = input().upper()

            test_case = int(input())
            token = list(map(int, input().strip().split()))

            for i in range(1, test_case+1):
                print(string[token[i-1]-1], end='')
            print()
    except EOFError:
        exit()


if __name__ == '__main__':
    math()
