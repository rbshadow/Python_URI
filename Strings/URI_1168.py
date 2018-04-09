def math():
    loop = int(input())

    for i in range(loop):
        i_put = input()
        count = 0

        for j in range(len(i_put)):
            if int(i_put[j]) == 1:
                count += int(i_put[j]) + 1
            elif int(i_put[j]) == 2:
                count += int(i_put[j]) + 3
            elif int(i_put[j]) == 3:
                count += int(i_put[j]) + 2
            elif int(i_put[j]) == 4:
                count += int(i_put[j]) + 0
            elif int(i_put[j]) == 5:
                count += int(i_put[j]) + 0
            elif int(i_put[j]) == 6:
                count += int(i_put[j]) + 0
            elif int(i_put[j]) == 7:
                count += int(i_put[j]) - 4
            elif int(i_put[j]) == 8:
                count += int(i_put[j]) - 1
            elif int(i_put[j]) == 9:
                count += int(i_put[j]) - 3
            elif int(i_put[j]) == 0:
                count += int(i_put[j]) + 6
        print(count, 'leds')


if __name__ == '__main__':
    math()
