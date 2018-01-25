def math():
    salary = input()
    salary_fl = float(salary).__format__('.2f')

    if 0.00 <= float(salary) <= 400.00:
        increase = .15
        increase_salary = (float(salary) * increase).__format__('.2f')
        total = (float(salary) + float(increase_salary)).__format__('.2f')
        print('Novo salario:', total)
        print('Reajuste ganho:', increase_salary)
        print('Em percentual: 15 %')

    if 400.01 <= float(salary) <= 800.00:
        increase = .12
        increase_salary = (float(salary) * increase).__format__('.2f')
        total = (float(salary) + float(increase_salary)).__format__('.2f')
        print('Novo salario:', total)
        print('Reajuste ganho:', increase_salary)
        print('Em percentual: 12 %')

    if 800.01 <= float(salary) <= 1200.00:
        increase = .10
        increase_salary = (float(salary) * increase).__format__('.2f')
        total = (float(salary) + float(increase_salary)).__format__('.2f')
        print('Novo salario:', total)
        print('Reajuste ganho:', increase_salary)
        print('Em percentual: 10 %')

    if 1200.01 <= float(salary) <= 2000.00:
        increase = .07
        increase_salary = (float(salary) * increase).__format__('.2f')
        total = (float(salary) + float(increase_salary)).__format__('.2f')
        print('Novo salario:', total)
        print('Reajuste ganho:', increase_salary)
        print('Em percentual: 7 %')

    if float(salary) > 2000.00:
        increase = .04
        increase_salary = (float(salary) * increase).__format__('.2f')
        total = (float(salary) + float(increase_salary)).__format__('.2f')
        print('Novo salario:', total)
        print('Reajuste ganho:', increase_salary)
        print('Em percentual: 4 %')


if __name__ == '__main__':
    math()
