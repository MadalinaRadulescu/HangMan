import random
import string
print("Welcome to the Hangman game")


# def select_difficulty():
#     print("Would you like to play difficulty 1(easy), 2(medium), or 3(hard)?")
#     level = int(input("Select difficulty: "))
#     lives = 0
#     while True:
#         if level == 1:
#             lives += 10
#             print("\nAwesome! We'll begin with easy! You have 10 lives")
#             break
#         elif level == 2:
#             lives += 7
#             print("\nAwesome! We'll begin with medium!You have 7 lives")
#             break
#         elif level == 3:
#             lives += 5
#             print("\nAwesome! We'll begin with hard!You have 5 lives")
#             break
#         else:
#             print("Invalid input!\nPlease enter either 1, 2 or 3. ")



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
    lives = select_difficulty()

    while len(secretword_letters) > 0 and lives > 0:
            
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
            else:
                lives = lives - 1
                print("Letter is not in word")
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
        while True:
            if level == 1:
                lives += 10
                print("\nAwesome! We'll begin with easy! You have 10 lives")
                break
            elif level == 2:
                lives += 7
                print("\nAwesome! We'll begin with medium!You have 7 lives")
                break
            elif level == 3:
                lives += 5
                print("\nAwesome! We'll begin with hard!You have 5 lives")
                break
            else:
                print("Invalid input!\nPlease enter either 1, 2 or 3. ")


if __name__ == "__main__":
    
    hangman()


