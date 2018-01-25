def math():
    a, b, c = map(float, input().split())

    maximum = max(a, b, c)
    minimum = min(a, b, c)
    final = (a + b + c) - maximum - minimum
    final = final.__format__('.1f')

    A = maximum
    B = final
    C = minimum

    if float(A) > 0.0 and float(B) > 0.0 and float(C) > 0.0:
        if float(A) >= (float(B) + C):
            print('NAO FORMA TRIANGULO')

        elif pow(float(A), 2) == (pow(float(B), 2) + pow(float(C), 2)):
            print('TRIANGULO RETANGULO')

        elif pow(float(A), 2) > (pow(float(B), 2) + pow(float(C), 2)):
            print('TRIANGULO OBTUSANGULO')

        elif pow(float(A), 2) < (pow(float(B), 2) + pow(float(C), 2)):
            print('TRIANGULO ACUTANGULO')

        if float(A) == float(B) == float(C):
            print('TRIANGULO EQUILATERO')

        if (float(A) == float(B) and float(A) != float(C)) or (float(B) == float(C) and float(B) != float(A)) or (float(C) == float(A) and float(C) != float(B)):
            print('TRIANGULO ISOSCELES')


if __name__ == '__main__':
    math()
