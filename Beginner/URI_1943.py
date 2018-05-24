def math():
    number = int(input())

    if number <= 1:
        print('Top 1')
    elif number <= 3:
        print('Top 3')
    elif number <= 5:
        print('Top 5')
    elif number <= 10:
        print('Top 10')
    elif number <= 25:
        print('Top 25')
    elif number <= 50:
        print('Top 50')
    elif number <= 100:
        print('Top 100')


if __name__ == '__main__':
    math()
