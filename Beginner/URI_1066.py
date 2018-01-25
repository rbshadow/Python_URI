def math():
    even_count = 0
    odd_count = 0
    pos_count = 0
    neg_count = 0

    for i in range(5):
        i = int(input())

        if i % 2 == 0:
            even_count = even_count + 1
        elif i % 2 == 1:
            odd_count = odd_count + 1

        if i < 0:
            neg_count = neg_count + 1
        elif i > 0:
            pos_count = pos_count + 1

    print(str(even_count), 'valor(es) par(es)' + '\n' +
          str(odd_count), 'valor(es) impar(es)' + '\n' +
          str(pos_count), 'valor(es) positivo(s)' + '\n' +
          str(neg_count), 'valor(es) negativo(s)')


if __name__ == '__main__':
    math()
