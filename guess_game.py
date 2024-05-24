import random


def run_guess(guess, answer):
    try:
        if 0 < guess < 11:
            if guess == answer:
                print('You got it! Congrats genius')
                return True
            else:
                print('Sorry, try again')
        else:
            print('Hey bozo, I said 1~10')
            return False
    except TypeError as err:
        print('Please enter a number. Run it again bozoman')
        return err


if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        guess = int(input('Guess a number 1~10: '))
        if (run_guess(guess, answer)):
            break
