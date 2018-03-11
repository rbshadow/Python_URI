def math():
    count = 0

    li_st = input().split()

    for i in li_st[1:]:
        if int(i) <= 0:
            li_st.remove(i)

    start = li_st[0]
    trav = li_st[1]

    end = int(start) + int(trav)
    for i in range(int(start), end):
        count += i
    print(count)


if __name__ == '__main__':
    math()
