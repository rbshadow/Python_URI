
def math():
    a = float(input())
    b = float(input())

    update_a = a * 3.5
    update_b = b * 7.5

    result = ((update_a + update_b) / (3.5+7.5)).__format__('.5f')
    print('MEDIA =', result)


if __name__ == '__main__':
    math()