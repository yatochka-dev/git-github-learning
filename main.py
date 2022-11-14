import random
from string import Template


class QuizGame(object):
    def __init__(self, random_number: int):
        self._random_number = random_number

    def start_game(self):
        print("Welcome to the quiz game!")
        print("Guess a number between 1 and 10")
        self._guess_number()

    def _guess_number(self):
        guess = int(input("Your guess: "))
        if guess == self._random_number:
            tm = Template(
                "You guessed correctly!\n The number was " "$number!"
            ).substitute({"number": self._random_number})
            print(tm)
        else:
            print("You guessed incorrectly!")
            self._guess_number()


def main():
    game = QuizGame(random.randint(1, 10))
    game.start_game()


if __name__ == "__main__":
    main()
