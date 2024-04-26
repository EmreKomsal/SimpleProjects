import pandas as pd

alphabet_data = pd.read_csv("PythonProjects/SimpleProjects/DataProjects/NATO-alphabet/nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}

convert = True

while convert:
    if input("Do you want to convert a word to NATO alphabet? (Y/N): ").upper() == "N":
        convert = False
        break
    else:
        user_input = input("Enter a word: ").upper()
        if not user_input.isalpha():
            print("Please enter a valid word")
            continue
        user_input_list = list(user_input)
        nato_list = [alphabet_dict[letter] for letter in user_input_list]
        print(nato_list)
