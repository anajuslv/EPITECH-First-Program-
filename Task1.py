import random
from english_words import english_words_lower_set


def check_penalties(penalties, word):
    if penalties >= 12:
        print("YOU LOSE!")
        print("THE WORD WAS:", word)
        return True
    return False


def random_word():
    return random.choice(list(english_words_lower_set)).upper()


def display_word(word, tested_letters):
    result = ""

    for letter in word:
        if letter in tested_letters:
            result = result + letter + " "
        else:
            result = result + "_ "

    print(result)


def hangman():
    word = random_word()
    tested_letters = []
    penalties = 0

    print("GAME STARTED!")

    while penalties < 12:

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

        if check_penalties(penalties, word):
            return

hangman()

