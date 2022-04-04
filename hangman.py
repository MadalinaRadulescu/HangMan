# PART 1
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
# sample data, normally the user should choose the difficulty
from operator import truediv
import random
words = ""
f = open("countries-and-capitals.txt")
lines = f.readlines()
words = random.choice(lines)
wordposition = words.index(" | ")
word_to_guess = words[0:wordposition]
print(word_to_guess)


# import random
hello = input("Hello ! Welcome to hangman!")
play = True
difficulty = "1"
while play:
    level = int(input('Pick a level of difficulty 1(easy), 2(medium), 3(hard): '))
    if level == 1:
        print ("Awesome! We'll begin with easy! You have 10 lives.")
        top = 100
        tries = 10
        break
    elif level == 2:
        print ("Awesome! We'll begin with medium! You have 7 lives.")
        top = 100
        tries = 7
        break
    elif level == 3:
        print ("Awesome! We'll begin with hard! You have 5 lives")
        top = 100
        tries = 5
        break
    else:
        top = 100
        tries = 10
    # if level == 1:
    #     print ("Awesome! We'll begin with easy!")
    # if level == 2:
    #     print ("Awesome! We'll begin with medium!")
    # if level == 3:
    #     print ("Awesome! We'll begin with hard!")
    if level != 1 and level != 2 and level != 3:
        print ("Invalid input!")
    

# STEP 2
# based on the chosen difficulty level, set the values 
# for the player's lives
word_to_guess = "Cairo" # sample data, normally the word should be chosen from the countries-and-capitals.txt
lives = 5 # sample data, normally the lives should be chosen based on the difficulty


# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" display "_ _ _ _ _"
# def displayBoard(missedLetters, correctLetters, secretWord):
#  print(HANGMAN_PICS[len(missedLetters)])
#  print()
# print('Missed letters:', end=' ')
#  for letter in missedLetters:
# print(letter, end=' ')
# print()
# blanks = '_' * len(secretWord)

# STEP 4
# ask the user to type a letter
# here you should validate if the typed letter is the word 
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions


# STEP 5
# validate if the typed letter is already in the tried letters
# HINT: search on the internet: `python if letter in list`
# If it is not, than append to the tried letters
# If it has already been typed, return to STEP 5. HINT: use a while loop here
already_tried_letters = [] # this list will contain all the tried letters


# STEP 6
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".


# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.



# STEP 7
# check if the variable already_tried_letters already contains all the letters necessary
# to build the value in the variable word_to_guess. If so display a winning message and exit
# the app.
# If you still have letters that are not guessed check if you have a non negative amount of lives
# left. If not print a loosing message and exit the app.
# If neither of the 2 conditions mentioned above go back to STEP 4
