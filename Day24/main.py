CURRENT_NAME = "[name]"

with open("./Input/Names/invited_names.txt", "r") as names:
    name_list = names.readlines()
    
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    content = letter.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter = content.replace(CURRENT_NAME, stripped_name)
        with open(f"./Output/ReadyToSend/Letter_to_{name}", "w") as final_letter:
            final_letter.write(new_letter)
