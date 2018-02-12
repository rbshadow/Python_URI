def math():
    count = 0
    for i in range(1, 101):
        count += 1/i
    res = count.__format__('.2f')
    print(res)


if __name__ == '__main__':
    math()
