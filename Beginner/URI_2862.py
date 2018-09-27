def insect():
    test_case = int(input())

    for i in range(test_case):
        number = int(input())

        if number > 8000:
            print('Mais de 8000!')
        elif number <= 8000:
            print('Inseto!')


if __name__ == '__main__':
    insect()
