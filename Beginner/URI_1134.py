def math():

    alco = 0
    gaso = 0
    dis = 0

    while True:
        x = int(input())
        if x <= 4:
            if x == 1:
                alco += 1
            elif x == 2:
                gaso += 1
            elif x == 3:
                dis += 1
            elif x == 4:
                print('MUITO OBRIGADO')
                print('Alcool:', alco)
                print('Gasolina:', gaso)
                print('Diesel:', dis)
                break
        else:
            x = int(input())
            if x == 1:
                alco += 1
            elif x == 2:
                gaso += 1
            elif x == 3:
                dis += 1
            elif x == 4:
                print('MUITO OBRIGADO')
                print('Alcool:', alco)
                print('Gasolina:', gaso)
                print('Diesel:', dis)
                break


if __name__ == '__main__':
    math()
