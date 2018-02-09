def math():
    user_input = int(input())

    for i in range(1, user_input+1):
        print(i, pow(i, 2), pow(i, 3))
        print(i, pow(i, 2)+1, pow(i, 3)+1)


if __name__ == '__main__':
    math()
