def math():
    days = int(input())

    year = (days / 365)
    year = int(year)

    month = ((days % 365) / 30)
    month = int(month)

    day = ((days % 365) % 30)

    print(
        str(year) + ' ano(s)\n' +
        str(month) + ' mes(es)\n' +
        str(day) + ' dia(s)'
    )


if __name__ == '__main__':
    math()
