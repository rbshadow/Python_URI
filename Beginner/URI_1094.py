def math():
    test_case = int(input())

    c_count = 0
    r_count = 0
    s_count = 0

    for i in range(test_case):
        amount, character = input().split()
        amount, character = int(amount), str(character).upper()
        if 1 <= amount <= 15:
            if character == 'C':
                c_count += amount
            elif character == 'R':
                r_count += amount
            elif character == 'S':
                s_count += amount

    total_count = (c_count + r_count + s_count)

    c_parcent = ((c_count / total_count) * 100).__format__('.2f')
    r_parcent = ((r_count / total_count) * 100).__format__('.2f')
    s_parcent = ((s_count / total_count) * 100).__format__('.2f')

    print('Total: ' + str(total_count) + ' cobaias')
    print('Total de coelhos:', c_count)
    print('Total de ratos:', r_count)
    print('Total de sapos:', s_count)
    print('Percentual de coelhos: ' + str(c_parcent) + ' %')
    print('Percentual de ratos: ' + str(r_parcent) + ' %')
    print('Percentual de sapos: ' + str(s_parcent) + ' %')


if __name__ == '__main__':
    math()
