def math():
    count = 0
    calculate = 0
    while True:
        read_x = int(input())
        if read_x > 0:
            calculate += read_x
            count += 1
        else:
            break

    result = (calculate / count).__format__('.2f')
    print(result)


if __name__ == '__main__':
    math()
