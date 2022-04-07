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

    secretword = get_secretword(lines)
    secretword_letters = set(secretword)
    alphabet = (string.ascii_uppercase) + (string.ascii_lowercase)
    used_letter = set()
    lives = select_difficulty()
    correctletters = [] 
    while len(secretword_letters) > 0 and lives > 0:

        print("You have " + str(lives) + " lives left and you  used these wrong letters: " + ' '.join(used_letter))

        secretword_list = ""
        for i in secretword:
            if i not in correctletters and i != " ":
                secretword_list += " _ "
            elif i == " ":
                secretword_list += "    "
            else:
                secretword_list += i

        print("Current word: " + ' '.join(secretword_list))
        guess_letter = input("\nGuess a letter: ")

        if guess_letter.upper() == "QUIT":
            quit()

        if guess_letter in alphabet:

            if guess_letter.lower() != used_letter and guess_letter.upper() != used_letter:

                if guess_letter.upper() in secretword_letters:
                    secretword_letters.remove(guess_letter.upper())
                    correctletters.append(guess_letter.upper())
                    

                if guess_letter.lower() in secretword_letters:
                    secretword_letters.remove(guess_letter.lower())
                    correctletters.append(guess_letter.lower())
                    

                elif guess_letter.lower() in used_letter or guess_letter.upper() in used_letter:
                    print("You already used that character. Please try again")

                else:
                    lives = lives - 1
                    used_letter.add(guess_letter)
                    print("Letter is not in word")
                    print(hangmanpic.HANGMANPICS[6 - lives])
                    # print("You have " + str(lives) + " lives left")

        elif guess_letter == " " and guess_letter in secretword_letters:
            secretword_letters.remove(guess_letter)
            used_letter.add(guess_letter)

        else:
            print("Invalid input. Please try again.")

    if lives == 0:
        print("You died, sorry. The word was " + secretword + "!")
    else:
        print("You guessed the word " + secretword + "!!")


def select_difficulty():

    print("Would you like to play difficulty 1(easy), 2(medium), or 3(hard)?")
    while True:
        level = input("Select difficulty: ")
        lives = 0
        try:
            level = int(level)
            break
        except ValueError:
            print("Thats not an integer")

    if level == 1:
        lives += 7
        print("\nAwesome! We'll begin with easy! You have 7 lives")
        return lives

    elif level == 2:
        lives += 5
        print("\nAwesome! We'll begin with medium!You have 5 lives")
        return lives

    elif level == 3:
        lives += 3
        print("\nAwesome! We'll begin with hard!You have 3 lives")
        return lives

    else:
        print("Invalid input!\nPlease enter either 1, 2 or 3. ")
        return select_difficulty()


hangman()
