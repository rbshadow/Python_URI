def math():
    i_h, i_m, f_h, f_m = map(int, input().strip().split())

    if i_h == i_m == f_h == f_m:
        print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')

    else:
        i_minutes = (i_h * 60) + i_m
        f_minutes = (f_h * 60) + f_m

        if i_h == f_h:
            min_calculator = (24 * 60) - (i_minutes - f_minutes)
        elif i_h > f_h:
            min_calculator = (i_minutes - f_minutes) - (24 * 60)
        elif i_h == i_m == f_h:
            min_calculator = (24 * 60) - (i_minutes - f_minutes)
        else:
            min_calculator = i_minutes - f_minutes

        absolute_minutes = abs(min_calculator)
        if absolute_minutes > 59:
            hour = absolute_minutes / 60
            minute = absolute_minutes % 60

            if hour < 24:
                print('O JOGO DUROU', int(hour), 'HORA(S) E', int(minute), 'MINUTO(S)')
            else:
                print('O JOGO DUROU 0 HORA(S) E', int(minute), 'MINUTO(S)')
        else:
            print('O JOGO DUROU 0 HORA(S) E', absolute_minutes, 'MINUTO(S)')


if __name__ == '__main__':
    math()
