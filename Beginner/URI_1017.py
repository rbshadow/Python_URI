def math():
    time = int(input())
    speed = int(input())

    result = (time * (speed / 12)).__format__('.3f')
    print(result)


if __name__ == '__main__':
    math()
