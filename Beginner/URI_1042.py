def math():
    a, b, c = map(int, input().split())

    maximum = max(a, b, c)
    minimum = min(a, b, c)

    if maximum == c:
        if minimum == a:
            print(a, b, c, sep='\n')

    if maximum == c:
        if minimum == b:
            print(b, a, c, sep='\n')

    if maximum == b:
        if minimum == a:
            print(a, c, b, sep='\n')
    if maximum == b:
        if minimum == c:
            print(c, a, b, sep='\n')

    if maximum == a:
        if minimum == b:
            print(b, c, a, sep='\n')
    if maximum == a:
        if minimum == c:
            print(c, b, a, sep='\n')
    print()
    print(a, b, c, sep='\n')


if __name__ == '__main__':
    math()
