import random as r

def guess_letter():
    letter = input("Guess a letter: ")
    if len(letter) != 1:
        print("Please enter a single letter.")
        return guess_letter()
    if not letter.isalpha():
        print("Please enter a letter.")
        return guess_letter()
    return letter.lower()

def main():
    print("Welcome to the hangman game!")
    life = 7
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]
    word = word_list[r.randint(0, len(word_list) - 1)]
    guessed = []
    if len(word) > 0:
        print("The word has", len(word), "letters.")
        for i in range(len(word)):
            guessed.append("_")
    print(guessed)
    while life > 0 and "_" in guessed:
        print(hangman_stages[7 - life])
        print("You have", life, "lives left.")
        letter = guess_letter()
        if letter in word:
            print("You guessed a letter correctly!")
            for i in range(len(word)):
                if word[i] == letter:
                    guessed[i] = letter
        else:
            print("You guessed a letter incorrectly!")
            life -= 1
        print(guessed)
    if "_" not in guessed:
        print("Congratulations! You guessed the word!")
    else:
        print("You ran out of lives! The word was", word)

# ASCII art for hangman stages
hangman_stages = [
    """
       _______
      |/      |
      |      
      |      
      |       
      |      
      |
     _|___
    """,
    """
       _______
      |/      |
      |      (_)
      |      
      |       
      |      
      |
     _|___
    """,
    """
       _______
      |/      |
      |      (_)
      |       |
      |       |
      |      
      |
     _|___
    """,
    """
       _______
      |/      |
      |      (_)
      |      \\|
      |       |
      |      
      |
     _|___
    """,
    """
       _______
      |/      |
      |      (_)
      |      \\|/
      |       |
      |      
      |
     _|___
    """,
    """
       _______
      |/      |
      |      (_)
      |      \\|/
      |       |
      |      / 
      |
     _|___
    """,
    """
       _______
      |/      |
      |      (_)
      |      \\|/
      |       |
      |      / \\
      |
     _|___
    """
]

if __name__ == "__main__":
    main()