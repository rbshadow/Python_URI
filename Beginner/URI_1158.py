def math():
    test_case = int(input())

    for i in range(test_case):
        count = 0
        count1 = 0
        read_x, n = map(int, input().split())
        x = read_x

        if read_x % 2 == 1:
            for j in range(n):
                if read_x % 2 == 1:
                    count += read_x
                read_x += 2
            print(count)

        if x % 2 == 0:
            for j in range(n):
                if x % 2 == 1:
                    count1 += x
                    x += 2
                else:
                    x += 1
            update_x = x
            result = count1 + update_x
            print(result)


if __name__ == '__main__':
    math()
