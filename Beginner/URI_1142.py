def math():
    user_input = int(input())

    for j in range(1, (user_input*4)+1):
        if j % 4 == 0:
            print('PUM')
        if j % 4 != 0:
            print(j, end=' ')


if __name__ == '__main__':
    math()
