def math():
    r = float(input())
    pi = 3.14159
    r = (r * r)
    result = (r * pi).__format__('.4f')
    print("A=", result, sep="")


if __name__ == '__main__':
    math()
