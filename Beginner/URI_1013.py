def math():
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)

    result = max(a, b, c)
    print(str(result) + ' eh o maior')


if __name__ == '__main__':
    math()
