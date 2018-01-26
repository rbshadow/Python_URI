def math():
    test_case = int(input())

    for i in range(test_case):
        x, y, z = map(float, input().split())
        x = (x * 2).__format__('.1f')
        y = (y * 3).__format__('.1f')
        z = (z * 5).__format__('.1f')
        result = ((float(x) + float(y) + float(z)) / 10.0).__format__('.1f')
        print(result)


if __name__ == '__main__':
    math()
