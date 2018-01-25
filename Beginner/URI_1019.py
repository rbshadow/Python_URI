def math():
    second = int(input())

    hours = (second / 3600)
    hours = int(hours)

    minutes = ((second % 3600) / 60)
    minutes = int(minutes)

    second = ((second % 60) % 60)
    second = int(second)

    print(hours, minutes, second, sep=':')


if __name__ == '__main__':
    math()
