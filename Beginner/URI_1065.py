def math():
    even_count = 0
    for i in range(5):
        i = int(input())

        if i % 2 == 0:
            even_count = even_count + 1
    print(even_count, 'valores pares')


if __name__ == '__main__':
    math()
