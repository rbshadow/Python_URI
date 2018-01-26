def math():
    up_one = int(input())
    up_two = int(input())

    count = 0

    if (up_one > up_two) and up_two < 0:
        for i in range(up_two, up_one):
            if i % 2 == 1:
                count = count + i
        print(count - up_two)

    elif (up_one < up_two) and up_one < 0:
        for i in range(up_one, up_two):
            if i % 2 == 1:
                count = count + i
        print(count - up_one)

    elif up_one > up_two:
        for i in range(up_two, up_one):
            if i % 2 == 1:
                count = count + i
        print(count)

    else:
        for i in range(up_one, up_two):
            if i % 2 == 1:
                count = count + i
        print(count)


if __name__ == '__main__':
    math()
