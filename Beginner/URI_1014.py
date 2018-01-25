def math():
    distance = int(input())
    fuel = float(input())

    result = (distance / fuel).__format__('.3f')
    print(str(result) + ' km/l')


if __name__ == '__main__':
    math()
