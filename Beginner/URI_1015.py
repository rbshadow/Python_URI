import math


def solve():
    a, b = map(float, input().split())
    c, d = map(float, input().split())

    power0 = c - a
    power1 = d - b

    result = (math.sqrt(pow(power0, 2) + pow(power1, 2))).__format__('.4f')
    print(result)


if __name__ == '__main__':
    solve()
