def math():

    m, n = map(int, input().split())
    count = 0

    if m > 0 and n > 0:
        if m < n:
            for i in range(m, n+1):
                count += i
                print(i, end=' ')
            print('Sum=' + str(count))
            math()
        elif n < m:
            for i in range(n, m+1):
                count += i
                print(i, end=' ')
            print('Sum=' + str(count))
            math()
        elif m == n:
            print(m, end=' ')
            print('Sum=' + str(m))
            math()
    else:
        exit()


if __name__ == '__main__':
    math()
