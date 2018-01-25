def math():
    a = float(input())
    b = float(input())
    c = float(input())

    update_a = a * 2
    update_b = b * 3
    update_c = c * 5

    result = ((update_a + update_b + update_c) / 10.0).__format__('.1f')
    print('MEDIA =', result)


if __name__ == '__main__':
    math()
