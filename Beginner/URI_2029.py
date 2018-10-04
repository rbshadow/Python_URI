def honey():
    while True:
        try:
            volume = input()
            diameter = input()

            volume = float(volume).__format__('.2f')
            diameter = float(diameter).__format__('.2f')
            pi = 3.14

            r = float(diameter) / 2

            height = (float(volume) / (pi * pow(r, 2)))
            area = pi * pow(r, 2)

            print('ALTURA =', height.__format__('.2f'))
            print('AREA =', area.__format__('.2f'))
        except EOFError:
            exit()


if __name__ == '__main__':
    honey()
