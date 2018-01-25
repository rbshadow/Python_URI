def math():
    a, b, c, d = map(float, input().split())

    a = a * 2
    b = b * 3
    c = c * 4
    d = d * 1

    avg = ((a + b + c + d) / 10).__format__('.1f')

    if float(avg) >= 7.0:
        print('Media:', avg)
        print('Aluno aprovado.')

    elif float(avg) < 5.0:
        print('Media:', avg)
        print('Aluno reprovado.')

    elif 5.0 <= float(avg) < 7.0:
        e = float(input())

        print('Media:', avg)
        print('Aluno em exame.')
        print('Nota do exame:', e.__format__('.1f'))

        avg = ((float(avg) + e) / 2.0).__format__('.1f')

        if float(avg) >= 5.0:
            print('Aluno aprovado.')

        elif float(avg) < 5.0:
            print('Aluno reprovado.')

        print('Media final:', avg)


if __name__ == '__main__':
    math()
