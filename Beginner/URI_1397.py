def math():

    while True:
        loop = int(input())
        count_a = 0
        count_b = 0
        if loop != 0:
            for i in range(loop):
                a, b = map(int, input().split())
                if a > b:
                    count_a += 1
                elif a < b:
                    count_b += 1
                else:
                    pass
            print(count_a, count_b)
        else:
            break


if __name__ == '__main__':
    math()
