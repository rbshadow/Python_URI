def math():
    i_put = int(input())

    final = hex(i_put)
    result = final.lstrip('0x')
    print(result.upper())


if __name__ == '__main__':
    math()
