gitfrom random import randint


def play_russian_roulette():
    if randint(0, 6) == 3:
        print("BANG!")
        exit()
    else:
        print("You got lucky this time")


def main():
    answer = 'Y'
    while answer != 'N':
        answer = input("Feeling lucky, punk? (Y/N) ")
        play_russian_roulette()
    print("It was nice playing with you")


if __name__ == '__main__':
    main()
