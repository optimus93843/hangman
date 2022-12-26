# import libraries

import random
from words import word_list

# Functions


# This function will choose a word from our data base
def get_word():
    word = random.choice(word_list)
    return word.upper()


# This function will play the game based on the word that has been selected
def game(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Are you ready! Let's PLAY HANGMAN!!!")
    print(word_completion)
    print("\n")

    # In this loop we are letting our user to guess letters until ending the game
    # The game ends when the number of trials reach 6 or the user guesses the word
    while not guessed and tries > 0:
        guess = input("Please enter a letter or word: ").upper()

        # Input is one letter
        if len(guess) == 1 and guess.isalpha():
            # Repeat guess
            if guess in guessed_letters:
                print("You already guessed the letter", guess)

            # Wrong guess
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)

            # Right guess
            else:
                print("Good Job!,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [
                    i for i, letter in enumerate(word) if letter == guess
                ]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        # Input is a word
        elif len(guess) == len(word) and guess.isalpha():

            # Repeat guess
            if guess in guessed_words:
                print(" You already guessed the word", guess)

            # Wrong guess
            elif guess != word:
                print(guess, "is not the word.")

            # Right word
            else:
                print("Good Job!,", guess, "is the word!")
                guessed = True
                word_completion = word

        # Input is not valid
        else:
            print("Not a valid guess.")

        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word correctly! YOU  WIN!")
        print("\n")
    else:
        print("Sorry, you ran out of tries,The word was " + word +
              ". Maybe next time!")
        print("YOU LOOSE!")
        print("\n")


# This function will display the hanging man
#def display_hangman(tries):

# Main code
word = get_word()
game(word)

while input("Do you want to play again? (Yes/No)").upper() == "YES":
    word = get_word()
    game(word)
print("Good bye! Game is finished!!!")
