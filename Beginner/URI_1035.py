def math():
    a, b, c, d = input().split()
    a, b, c, d = int(a), int(b), int(c), int(d)

    sum0 = c + d
    sum1 = a + b

    if b > c and d > a:
        if sum0 > sum1:
            if c > -1 and d > -1:
                if (a % 2) == 0:
                    print('Valores aceitos')
                else:
                    print('Valores nao aceitos')
            else:
                print('Valores nao aceitos')
        else:
            print('Valores nao aceitos')
    else:
        print('Valores nao aceitos')


if __name__ == '__main__':
    math()
