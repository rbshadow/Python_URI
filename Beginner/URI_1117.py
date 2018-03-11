def math():
    read_list = []
    while True:
        read_input = float(input())

        if read_input < 0:
            print('nota invalida')
        elif read_input > 10:
            print('nota invalida')
        else:
            read_list.append(read_input)
            if len(read_list) == 2:
                res = ((read_list[0] + read_list[1]) / 2).__format__('.2f')
                print('media =', res)
                exit()


if __name__ == '__main__':
    math()
