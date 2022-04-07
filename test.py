def get_list():
    word = "Burundi"
    list = set(word)
    if " " in list:
        list.remove(" ")
    return list

print(get_list())
