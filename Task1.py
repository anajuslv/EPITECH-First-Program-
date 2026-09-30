import random
import argparse
from english_words import english_words_lower_set


def check_penalties(penalties, max_penalties, word):
    if penalties >= max_penalties:
        print("YOU LOSE!")
        print("THE WORD WAS:", word)
        return True

    return False


def random_word(word_list, word_length):
    words = []

    for word in word_list:
        if len(word) == word_length:
            words.append(word.upper())

    return random.choice(words)


def display_word(word, tested_letters):
    result = ""

    for letter in word:
        if letter in tested_letters:
            result = result + letter + " "
        else:
            result = result + "_ "

    print(result)


def hangman(max_penalties, word_length):
    word = random_word(english_words_lower_set, word_length)

    tested_letters = []
    penalties = 0

    print("GAME STARTED!")

    while penalties <= max_penalties:

        print()
        display_word(word, tested_letters)

        print("TESTED LETTERS:", " ".join(tested_letters))
        print(penalties, "PENALTIES")

        guess = input("$> ").upper()

        if len(guess) == 1:

            if guess in tested_letters:
                print("You already tested this letter!")
                continue

            tested_letters.append(guess)

            if guess in word:
                print("FOUND ONE '" + guess + "'")
            else:
                print("NO '" + guess + "' FOUND")
                penalties = penalties + 1

        else:

            if guess == word:
                print(guess + ": CORRECT GUESS")
                print("-", penalties, "PENALTIES")
                return
            else:
                print(guess + ": INCORRECT GUESS")
                penalties = penalties + 5

        if all(letter in tested_letters for letter in word):
            print()
            print(word + ": CORRECT GUESS")
            print("-", penalties, "PENALTIES")
            return

        if check_penalties(penalties, max_penalties, word):
            return


parser = argparse.ArgumentParser()

parser.add_argument(
    "--penalties",
    type=int,
    default=12
)

parser.add_argument(
    "--length",
    type=int,
    default=5
)

args = parser.parse_args()

hangman(args.penalties, args.length)

