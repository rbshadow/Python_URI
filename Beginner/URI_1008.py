def math():
    number = int(input())
    work_hour = int(input())
    amount = float(input())
    salary = (work_hour * amount).__format__('.2f')

    print('NUMBER =', number)
    print('SALARY = U$', salary)


if __name__ == '__main__':
    math()
