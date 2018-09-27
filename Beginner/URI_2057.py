def timezone():

    deparature, travel, destination = map(int, input().strip().split())

    travel_time = deparature + travel + destination

    if travel_time < 0:
        travel_time = 24 + travel_time

    elif travel_time > 24:
        travel_time = travel_time - 24

    elif travel_time == 24:
        travel_time = 0

    print(travel_time)


if __name__ == '__main__':
    timezone()
