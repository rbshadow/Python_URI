def math():
    try:
        while True:
            i_put = int(input())
            item = list(map(int, input().strip().split()))
            speed = max(item)

            if int(speed) < 10:
                print('1')
            elif 10 <= int(speed) < 20:
                print('2')
            elif int(speed) >= 20:
                print('3')
    except EOFError:
        exit()


if __name__ == '__main__':
    math()
