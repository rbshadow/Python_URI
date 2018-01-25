def math():
    first = input().lower()
    second = input().lower()
    third = input().lower()

    # First Option

    if first == 'vertebrado':
        if second == 'ave':
            if third == 'carnivoro':
                print('aguia')

    if first == 'vertebrado':
        if second == 'ave':
            if third == 'onivoro':
                print('pomba')

    if first == 'vertebrado':
        if second == 'mamifero':
            if third == 'onivoro':
                print('homem')

    if first == 'vertebrado':
        if second == 'mamifero':
            if third == 'herbivoro':
                print('vaca')

    # Second Option

    if first == 'invertebrado':
        if second == 'inseto':
            if third == 'hematofago':
                print('pulga')

    if first == 'invertebrado':
        if second == 'inseto':
            if third == 'herbivoro':
                print('lagarta')

    if first == 'invertebrado':
        if second == 'anelideo':
            if third == 'hematofago':
                print('sanguessuga')

    if first == 'invertebrado':
        if second == 'anelideo':
            if third == 'onivoro':
                print('minhoca')


if __name__ == '__main__':
    math()
