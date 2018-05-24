def math():
    number_list = []

    while True:
        i_put = float(input()).__format__('.2f')

        if 0.0 <= float(i_put) <= 10.0:
            number_list.append(float(i_put))
        else:
            print('nota invalida')

        media = 0.00
        if len(number_list) == 2:
            for i in number_list:
                media += i
            print('media = {}'.format((media/2).__format__('.2f')))

            while True:
                print('novo calculo (1-sim 2-nao)')
                select_choice = int(input())

                if select_choice == 1:
                    math()
                elif select_choice == 2:
                    exit()


if __name__ == '__main__':
    math()
