


def display(secretword, letters):
    result = ""
    for i in secretword:
        if i not in letters and i != " ":
            result += " _ "
            #secretword.replace(i, " _ ")
        elif i == " ":
            result += " "
        else:
            result += i
    print(result)
        







secretword = "Code     cool"
guessed_letters=["c", "d"]

display(secretword, guessed_letters)

# C _ d _  c _ _ _
print("You have " + str(lives) + " lives left and you used these letters: " + ' '.join(used_letter))
        secretword_list = [letter if letter in used_letter else " _ " for letter in secretword]

        print("Current word: " + ' '.join(secretword_list))
 guess_letter = input("Guess a letter: ")
        if guess_letter.upper() == "QUIT":
            quit()
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
                # print("You have " + str(lives) + " lives left")
        else:
            print("Invalid input. Please try again.")

    if lives == 0:
        print("You died, sorry. The word was " + secretword + "!")
    else:
        print("You guessed the word " + secretword + "!!")

