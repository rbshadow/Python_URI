def math():
    s = 1
    s1 = 2
    count = 0
    for i in range(1, 40):
        s = (s + 2)
        res = (s/s1)
        count += res
        s1 = (s1 + s1)
    result = (1+count).__format__('.2f')
    print(result)


if __name__ == '__main__':
    math()
