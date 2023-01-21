#Name: Hassan Azam
#Assignment: Computer Science Final Culminating
#Class: Mr.Tombs
#Course code: ICS3UR
#School: Port Credit Secondary School
#Due Date: January 20, 2023





# import libraries

import random   #This makes the game select random words from word.py
import words    #This library contains all the words that we will use in the game
from display import display_hangman     #This imports the display of the hangman game
from display import display_scores      #This imports the display of the score board
from level import select_level
import login    #This imports the login page 
import os   #Controls operating system
import menu     #imports the menus here

# Functions


# This function will choose a word from our data base
def get_word(game_level):
    if game_level == "easy":
        word = random.choice(words.word_list_easy)
    elif game_level == "medium":
        word = random.choice(words.word_list_medium)
    else:
        word = random.choice(words.word_list_hard)
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

        #This updates the file which is the scoreboard in this case
        if user in main_file.keys():
            main_file[user] += 1
        else:
            main_file[user] = 1

        
        #Removes the old score by replacing the new recent score which the user got 
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

        #Updates Scoreboard by removing the old score which the user previosuly got
        if user in main_file.keys():
            main_file[user] -= 1
        else:
            main_file[user] = 0

        

        for user_name in main_file:
            f_temp.write(user_name + ',' + str(main_file[user_name])+'\n')

        f_temp.close()
        f_main.close()

        os.remove("score_board.txt")
        os.rename("temp.txt","score_board.txt")


# Puts a score in the scoreboard file/text and displays it to the user
score_board = {}
menu.menu_pygame()
login_tries = 3
result_login = login.login_pygame(login_tries)
login_tries -=1
username = result_login[1]


while login_tries >0:
    if result_login[0] == False:
        result_login = login.login_pygame(login_tries)
        login_tries -= 1
    else:
        break
#This is for the username and password to see if the user got their correct username and password
if result_login[0]:
    #level = input("Which level do you choose? (easy/medium/hard): ")
    level = select_level()
    word = get_word(level)
    game(word,username)

#This just ask the user wether or not if they want to play again and if they want to see the scoreboard
    while input("Do you want to play again? (Yes/No)").upper() == "YES":
        # level = input("Which level do you choose? (easy/medium/hard): ")
        level = select_level()
        word = get_word(level)
        game(word,username)
        
if input("Do you want to see the score_board? (Yes/No)").upper() == "YES":
    with open ("score_board.txt") as f:
        for line in f:
        
            (key, val) = line.split(",")
            score_board[key] = val
    display_scores(score_board)
    # our scores are saved in score_board dictionary
    # for score in score_board:
    #     print("User name: " + score + '---'+"Score: " +  score_board[score] )


#The End
print("Good bye! Game is finished!!!")
