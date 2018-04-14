def math():
    i_put = input().split('.')

    for i in i_put:
        if '-' in i:
            j = i.split('-')
            for k in j:
                print(k)
        else:
            print(i)


if __name__ == '__main__':
    math()
