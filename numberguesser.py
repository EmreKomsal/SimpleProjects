import random

def number_guess(number, guess):
    # Check if the guess is too low
    if guess < number:
        return "Your guess is too low!"
    # Check if the guess is too high
    elif guess > number:
        return "Your guess is too high!"
    # The guess is correct
    else:
        return "Congratulations! You guessed the number!"
    
def guess_computer():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    guess = None
    attempts = 0
    print("Welcome to the Number Guesser game!")
    #Choose the number of attempts
    print("Choose your difficulty level: Easy, Medium, Hard")
    level = input("Enter your difficulty level: ")
    if level == "Easy":
        attempts = 10
    elif level == "Medium":
        attempts = 7
    elif level == "Hard":
        attempts = 5
    else:
        print("Invalid difficulty level. The game will be set to Easy.")
        attempts = 10
    while guess != number or attempts > 0:
        print("Guess the number between 1 and 100.")
        # Get the user's guess
        guess = int(input("Enter your guess: "))
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
        attempts -= 1
        # Check the user's guess
        print(number_guess(number, guess))
        if guess == number:
            break
        elif attempts == 0:
            break

    if attempts == 0:
        # The user ran out of attempts
        print("You ran out of attempts. The number was", number)
    else:
        # The user guessed the number
        print("You guessed the number in", attempts, "attempts.")
        
def guess_player():
    print("Welcome to the Number Guesser game!")
    print("please guess a number between 1 and 100")
    print("I will try to guess the number")
    still_guessing = True
    attempts = 0
    low = 1
    high = 100
    while still_guessing:
        guess = random.randint(low, high)
        print("My guess is:", guess)
        response = input("Is my guess too high, too low, or correct? ").lower()
        attempts += 1
        if response == "correct":
            print("I guessed the number in", attempts, "attempts.")
            still_guessing = False
        elif response == "low":
            low = guess     
        elif response == "high":
            high = guess
        elif response not in ["low", "high", "correct"]:
            print("Please enter too high, too low, or correct.")
            attempts -= 1
        
if __name__ == "__main__":
    print(""" 
  _   _  _    _  __  __  ____   ______  _____     _____  _    _  ______   _____  _____  ______  _____  
 | \ | || |  | ||  \/  ||  _ \ |  ____||  __ \   / ____|| |  | ||  ____| / ____|/ ____||  ____||  __ \ 
 |  \| || |  | || \  / || |_) || |__   | |__) | | |  __ | |  | || |__   | (___ | (___  | |__   | |__) |
 | . ` || |  | || |\/| ||  _ < |  __|  |  _  /  | | |_ || |  | ||  __|   \___ \ \___ \ |  __|  |  _  / 
 | |\  || |__| || |  | || |_) || |____ | | \ \  | |__| || |__| || |____  ____) |____) || |____ | | \ \ 
 |_| \_| \____/ |_|  |_||____/ |______||_|  \_\  \_____| \____/ |______||_____/|_____/ |______||_|  \_\\
""")
    print("Welcome to the Number Guesser game!")
    print("Do you want to guess the number or should I guess the number?")
    choice = input("Enter 'player' to guess the number or 'computer' to let the computer guess: ").lower()
    if choice == "player":
        guess_player()
    elif choice == "computer":
        guess_computer()
    else:
        print("Invalid choice. Please enter 'player' or 'computer'.")