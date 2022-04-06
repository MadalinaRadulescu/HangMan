import random
import string
import hangmanpic
print("Welcome to the Hangman game")

f = open("countries-and-capitals.txt")
lines = f.readlines()


def get_secretword(lines):
    word = ""
    word = random.choice(lines)
    wordposition = word.index(" | ")
    secretword = word[0:wordposition]
    return secretword


get_secretword(lines)


def hangman():
    secretword = "Republica Moldova"  # get_secretword(lines)
    secretword_letters = set(secretword)
    alphabet = (string.ascii_uppercase)
    used_letter = set()
    lives = select_difficulty()

    while len(secretword_letters) > 0 and lives > 0:
        print("You have used these letters: " + ' '.join(used_letter))
        secretword_list = [letter if letter in used_letter else " _ " for letter in secretword]

        print("Current word: " + ' '.join(secretword_list))
        guess_letter = input("Guess a letter: ")
        if guess_letter.upper() in alphabet or guess_letter == " ":
            if guess_letter.upper() in secretword_letters:
                used_letter.add(guess_letter.upper())
                secretword_letters.remove(guess_letter.upper())
            elif guess_letter.lower() in secretword_letters:
                used_letter.add(guess_letter.lower())
                secretword_letters.remove(guess_letter.lower())
            elif guess_letter in used_letter:
                used_letter.add(guess_letter)
                print("You already used that character. Please try again")
            else:
                lives = lives - 1
                print("Letter is not in word")
                print(hangmanpic.HANGMANPICS[6 - lives])
                print("You have " + str(lives) + " lives left")
        else:
            print("Invalid input. Please try again.")

    if lives == 0:
        print("You died, sorry. The word was " + secretword + "!")
    else:
        print("You guessed the word " + secretword + "!!")


def select_difficulty():
    print("Would you like to play difficulty 1(easy), 2(medium), or 3(hard)?")
    level = int(input("Select difficulty: "))
    lives = 0
    if level == 1:
        lives += 7
        print("\nAwesome! We'll begin with easy! You have 7 lives")
    elif level == 2:
        lives += 5
        print("\nAwesome! We'll begin with medium!You have 5 lives")
    elif level == 3:
        lives += 3
        print("\nAwesome! We'll begin with hard!You have 3 lives")
    else:
        print("Invalid input!\nPlease enter either 1, 2 or 3. ")

    return lives


hangman()
