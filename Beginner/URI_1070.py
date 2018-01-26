def math():
    user_input = int(input())

    if user_input % 2 == 0:
        for i in range(user_input, user_input+12, 2):
            print(i + 1)
    else:
        for i in range(user_input, user_input+12, 2):
            print(i)


if __name__ == '__main__':
    math()
