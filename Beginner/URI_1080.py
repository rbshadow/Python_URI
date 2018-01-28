def math():
    queue = []
    for i in range(100):
        i = int(input())
        queue.append(i)

    maximum = max(queue)
    position = queue.index(maximum)

    print(maximum)
    print(position+1)


if __name__ == '__main__':
    math()
