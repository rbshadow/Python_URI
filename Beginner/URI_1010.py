def math():
    a, b, c = input().split()
    d, e, f = input().split()

    update_a, update_b, update_c = int(a), int(b), float(c)
    update_d, update_e, update_f = int(d), int(e), float(f)

    result_1 = update_b * update_c
    result_2 = update_e * update_f
    final_result = (result_1 + result_2).__format__('.2f')

    print('VALOR A PAGAR: R$', final_result)


if __name__ == '__main__':
    math()
