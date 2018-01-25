def math():
    takas = input()
    taka = float(takas)

    hundred = taka / 100
    hundred_int = int(hundred)
    taka = taka % 100

    fifty = taka / 50
    fifty_int = int(fifty)
    taka = taka % 50

    twenty = taka / 20
    twenty_int = int(twenty)
    taka = taka % 20

    ten = taka / 10
    ten_int = int(ten)
    taka = taka % 10

    five = taka / 5
    five_int = int(five)
    taka = taka % 5

    two = taka / 2
    two_int = int(two)
    taka = taka % 2

    one = taka / 1
    one_int = int(one)
    taka = taka % 1

    fifty_paisa = taka / .50
    fifty_paisa_int = int(fifty_paisa)
    taka = taka % .50

    twenty_five_paisa = taka / .25
    twenty_five_paisa_int = int(twenty_five_paisa)
    taka = taka % .25

    ten_paisa = taka / .10
    ten_paisa_int = int(ten_paisa)
    taka = taka % .10

    five_paisa = taka / .05
    five_paisa_int = int(five_paisa)
    taka = taka % .05

    taka = taka.__format__('.2f')
    one_paisa = float(taka) / .01
    one_paisa_int = int(one_paisa)

    print('NOTAS:')
    print(str(hundred_int) + ' nota(s) de R$ 100.00')
    print(str(fifty_int) + ' nota(s) de R$ 50.00')
    print(str(twenty_int) + ' nota(s) de R$ 20.00')
    print(str(ten_int) + ' nota(s) de R$ 10.00')
    print(str(five_int) + ' nota(s) de R$ 5.00')
    print(str(two_int) + ' nota(s) de R$ 2.00')
    print('MOEDAS:')
    print(str(one_int) + ' moeda(s) de R$ 1.00')
    print(str(fifty_paisa_int) + ' moeda(s) de R$ 0.50')
    print(str(twenty_five_paisa_int) + ' moeda(s) de R$ 0.25')
    print(str(ten_paisa_int) + ' moeda(s) de R$ 0.10')
    print(str(five_paisa_int) + ' moeda(s) de R$ 0.05')
    print(str(one_paisa_int) + ' moeda(s) de R$ 0.01')


if __name__ == '__main__':
    math()
