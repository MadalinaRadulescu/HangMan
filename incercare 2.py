


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


