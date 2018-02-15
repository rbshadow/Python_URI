def math():

    par = []
    no_par = []

    for i in range(15):
        j = int(input())

        if j % 2 == 0:
            par.append(j)
            l_par = len(par)
            if l_par == 5:
                for k in range(l_par):
                    print('par[' + str(k) + '] =', par[k])
                par = []
        else:
            no_par.append(j)
            nl_par = len(no_par)
            if nl_par == 5:
                for k in range(nl_par):
                    print('impar[' + str(k) + '] =', no_par[k])
                no_par = []

    nl_par = len(no_par)
    for k in range(nl_par):
        print('impar[' + str(k) + '] =', no_par[k])

    l_par = len(par)
    for k in range(l_par):
        print('par[' + str(k) + '] =', par[k])


if __name__ == '__main__':
    math()
