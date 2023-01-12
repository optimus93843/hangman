# import libraries

import random
from words import word_list
from display import display_hangman
import login
import os
import menu 

# Functions


# This function will choose a word from our data base
def get_word():
    word = random.choice(word_list)
    return word.upper()


# This function will play the game based on the word that has been selected
def game(word,user):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Are you ready! Let's PLAY HANGMAN!!!")
    print("Your user name is: ",user)
    print(display_hangman(tries))
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
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    # Player guessed correctly
    if guessed:
        print("Congrats, you guessed the word correctly! YOU  WIN!")
        print("\n")

        #update score board
        f_main = open("score_board.txt", "r")
        f_temp = open("temp.txt", "a")

        main_file = {}

        for line in f_main:
            (key, val) = line.split(",")
            main_file [key] = int(val[:-1])


        if user in main_file.keys():
            main_file[user] += 1
        else:
            main_file[user] = 1

        #print(main_file)

        for user_name in main_file:
            f_temp.write(user_name + ',' + str(main_file[user_name])+'\n')

        f_temp.close()
        f_main.close()

        os.remove("score_board.txt")
        os.rename("temp.txt","score_board.txt")
    
    # Player guessed incorrectly
    else:
        print("Sorry, you ran out of tries,The word was " + word +
              ". Maybe next time!")
        print("YOU LOOSE!")
        print("\n")

        # update score board
        f_main = open("score_board.txt", "r")
        f_temp = open("temp.txt", "a")

        main_file = {}

        for line in f_main:
            (key, val) = line.split(",")
            main_file [key] = int(val[:-1])


        if user in main_file.keys():
            main_file[user] -= 1
        else:
            main_file[user] = 0

        #print(main_file)

        for user_name in main_file:
            f_temp.write(user_name + ',' + str(main_file[user_name])+'\n')

        f_temp.close()
        f_main.close()

        os.remove("score_board.txt")
        os.rename("temp.txt","score_board.txt")


# Main code
score_board = {}
menu.menu_pygame()
result_login = login.login_pygame()
username = result_login[1]
if result_login[0]:
    #print("Let's play HANGMAN!")
    #if input("Do you want to start Hangman Game?").upper() == "YES":
    word = get_word()
    game(word,username)

    while input("Do you want to play again? (Yes/No)").upper() == "YES":
        word = get_word()
        game(word)
if input("Do you want to see the score_board? (Yes/No)").upper() == "YES":
    with open ("score_board.txt") as f:
        for line in f:
        #print(line)
            (key, val) = line.split(",")
            score_board[key] = val
    # username = input("Please enter your user name: ") 
    # if username in score_board.keys():
    #     print("Your score is: ", score_board[username])
    # else:
    #     print("There is no data for the user name.")
    for score in score_board:
        print("User name: " + score + '---'+"Score: " +  score_board[score] )

print("Good bye! Game is finished!!!")
