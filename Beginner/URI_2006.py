def math():
    tea = int(input())
    count = 0

    for i in range(1):
        guess = list(map(int, input().split()))
        length = len(guess)
        for j in range(length):
            if str(guess[j]) == str(tea):
                count += 1
    print(count)


if __name__ == '__main__':
    math()
