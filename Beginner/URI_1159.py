def math():
    while True:
        read = int(input())

        if read == 0:
            break
        else:
            count = 0
            for j in range(read, read+9, 2):
                if j % 2 == 0:
                    count += j
                else:
                    j += 1
                    count += j
            print(count)


if __name__ == '__main__':
    math()
