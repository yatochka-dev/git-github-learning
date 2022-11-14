import random


class WordQuiz(object):

    def __init__(
            self,
            word_list: list,
            number_of_guesses: int,
            number_of_words: int,
    ):
        self._word_list = word_list
        self._number_of_guesses = number_of_guesses
        self._number_of_words = number_of_words
        self._words = []
        self._guesses = []
        self._correct = []
        self._incorrect = []
        self._score = 0
        self._word = None
        self._guess = None
        self._correct_guesses = 0
        self._incorrect_guesses = 0
        self._guesses_left = 0
        self._guesses_left = self._number_of_guesses

    def start_game(self):
        print("Welcome to the word quiz game!")
        print("Guess a word from the list")
        self._generate_words()
        self._guess_word()

    def _generate_words(self):
        for i in range(self._number_of_words):
            self._words.append(random.choice(self._word_list))

    def _guess_word(self):
        self._word = random.choice(self._words)
        self._guesses_left = self._number_of_guesses
        while self._guesses_left > 0:
            self._guess = input("Your guess: ")
            if self._guess == self._word:
                self._correct_guesses += 1
                self._correct.append(self._word)
                self._words.remove(self._word)
                self._guesses_left = 0
            else:
                self._incorrect_guesses += 1
                self._incorrect.append(self._word)
                self._words.remove(self._word)
                self._guesses_left -= 1
        self._score = self._correct_guesses / self._number_of_words
        self._print_score()

    def _print_score(self):
        print("Your score was: {}".format(self._score))
        print("You guessed {} words correctly".format(self._correct_guesses))
        print(
            "You guessed {} words incorrectly".format(self._incorrect_guesses))
        print("You guessed the following words correctly: {}".format(
            self._correct))
        print("You guessed the following words incorrectly: {}".format(
            self._incorrect))


def main():
    quiz = WordQuiz(
        word_list=["cat", "dog", "bird", "fish", "snake", "lizard"],
        number_of_guesses=3,
        number_of_words=5,
    )
    quiz.start_game()


if __name__ == '__main__':
    main()
