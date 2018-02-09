def math():
    user_line, user_number = map(int, input().split())

    for i in range(1, user_number+1):
        if i % user_line == 0:
            print(i)
        if i % user_line != 0:
            print(i, end=' ')


if __name__ == '__main__':
    math()
