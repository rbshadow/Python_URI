def math():
    i_put = input().strip()
    for i in i_put[::-1]:
        print(i, end='')
    print()


if __name__ == '__main__':
    math()
