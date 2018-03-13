def math():
    test_case = int(input())

    li_st = list(map(int, input().strip().split()))
    minimum = 0
    pos = 0
    if 1 <= test_case <= 1000:
        for i in range(len(li_st)):
            minimum = min(li_st)
            pos = li_st.index(minimum)
        print('Menor valor:', minimum)
        print('Posicao:', pos)
    else:
        pass


if __name__ == '__main__':
    math()
