# PART 1
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
#difficulty = "1" # sample data, normally the user should choose the difficulty
import random
import string


f = open("countries-and-capitals.txt")
lines = f.readlines()

def get_secretword(lines):
    word = ""
    word = random.choice(lines)
    wordposition = word.index(" | ")
    secretword = word[0:wordposition]
    return secretword.upper()

get_secretword(lines)


def hangman():
    secretword = get_secretword(lines)
    secretword_letters = set(secretword)
    alphabet = (string.ascii_uppercase)
    used_letter = set()
    while len(secretword_letters)>0:
        
        print("You have used these letters: " + ' '.join(used_letter))
        secretword_list = [letter if letter in used_letter else " _ " for letter in secretword]
        print("Current word: " + ' '.join(secretword_list))
        guess_letter = raw_input("Guess a letter: ").upper()
        if guess_letter in alphabet:
            used_letter.add(guess_letter)
            if guess_letter in secretword_letters:
                secretword_letters.remove(guess_letter)
            elif guess_letter in used_letter:
                print("You already used that character. Please try again")
        elif guess_letter == " ":
            used_letter.add(" ")
        else:
            print("Input invalid. Plese try again!")
            
    print("You guessed the word " + secretword + "!!")
hangman()
    # if level == 1:
    #     print ("Awesome! We'll begin with easy!")
    # if level == 2:
    #     print ("Awesome! We'll begin with medium!")
    # if level == 3:
    #     print ("Awesome! We'll begin with hard!")
    

# STEP 2
# based on the chosen difficulty level, set the values 
# for the player's lives
#word_to_guess = "Cairo" # sample data, normally the word should be chosen from the countries-and-capitals.txt
#lives = 5 # sample data, normally the lives should be chosen based on the difficulty


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
#already_tried_letters = [] # this list will contain all the tried letters


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
