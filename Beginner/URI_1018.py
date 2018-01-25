def math():
    taka = int(input())

    hundred = (taka / 100)
    hundred = int(hundred)

    fifty = ((taka % 100) / 50)
    fifty = int(fifty)

    twenty = (((taka % 100) % 50) / 20)
    twenty = int(twenty)

    ten = ((((taka % 100) % 50) % 20) / 10)
    ten = int(ten)

    five = (((((taka % 100) % 50) % 20) % 10) / 5)
    five = int(five)

    two = ((((((taka % 100) % 50) % 20) % 10) % 5) / 2)
    two = int(two)

    one = (((((((taka % 100) % 50) % 20) % 10) % 5) % 2) / 1)
    one = int(one)

    print(str(taka) + '\n' +
          str(hundred) + ' nota(s) de R$ 100,00' + '\n' +
          str(fifty) + ' nota(s) de R$ 50,00' + '\n' +
          str(twenty) + ' nota(s) de R$ 20,00' + '\n' +
          str(ten) + ' nota(s) de R$ 10,00' + '\n' +
          str(five) + ' nota(s) de R$ 5,00' + '\n' +
          str(two) + ' nota(s) de R$ 2,00' + '\n' +
          str(one) + ' nota(s) de R$ 1,00'
          )


if __name__ == '__main__':
    math()
