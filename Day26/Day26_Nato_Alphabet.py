import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter:row.code for (index, row) in alphabet.iterrows()}

user_input = input("Enter a word: ").upper()     

answer = [nato_alphabet[letter] for letter in user_input]
print(answer)


