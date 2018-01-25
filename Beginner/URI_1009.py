def math():
    name = input()
    salary = float(input())
    sold = float(input())

    bonus = (sold * .15)
    result = (salary + bonus).__format__('.2f')

    print('TOTAL = R$', result)


if __name__ == '__main__':
    math()
