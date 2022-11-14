import random


class QuizGame(object):

    def __init__(
            self
    ):
        self._random_number = random.randint(1, 10)

    def start_game(self):
        print("Welcome to the quiz game!")
        print("Guess a number between 1 and 10")
        self._guess_number()

    def _guess_number(self):
        guess = int(input("Your guess: "))
        if guess == self._random_number:
            print("You guessed correctly!")
        else:
            print("You guessed incorrectly!")
            self._guess_number()


def main():
    game = QuizGame()
    game.start_game()


if __name__ == "__main__":
    main()
