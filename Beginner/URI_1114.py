def math():
    password = int(input())

    while True:
        if password == 2002:
            print('Acesso Permitido')
            exit()
        else:
            print('Senha Invalida')
            math()


if __name__ == '__main__':
    math()
