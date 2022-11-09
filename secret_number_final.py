import random

print("Let the games commence \n")

def start():
    game_mode = input("Do you want to choose the number or can I? \n (Choose game mode 1 or 2)\n1-AI chooses the number\n2-AI guesses the number\n")
    if game_mode == "1":
        game_on_ai()
    elif game_mode == "2":
        game_on_user()
    else:
        print("Not a valid input")
        start()

def game_on_ai():
    guessed_right = False
    guess = ""
    guess_count = 0
    lowest = 1
    highest = int(input("Choose the upper limit (must be a whole number greater than 1)\n"))

    the_number = random.randint(lowest, highest)

    while not guessed_right:
        guess = input(f"Guess the number, between {lowest} and {highest}: \n")
        if int(guess) == int(the_number):
            print("\nThat's the number!\n")
            guessed_right = True
            guess_count += 1
        elif int(guess) < int(lowest):
            print(f"Try a number above {lowest}")
        elif int(guess) < int(the_number):
            print("\nToo low\n")
            lowest = guess
            guess_count += 1
        elif int(guess) > int(highest):
            print(f"Try a number below {highest}")
        elif int(guess) > int(the_number):
            print("\nToo high\n")
            highest = guess
            guess_count += 1
        else:
            print("Your input was not valid\n\n")
    if guess_count > 1:
        print(f"You got the number in {guess_count} guesses.")
    else:
        print(f"You got the number in {guess_count} guess.")
    check_again()
    

def game_on_user():
    guessed_right = False
    guess = ""
    guess_count = 0
    lowest = 1
    highest = int(input("Choose the upper limit (must be a whole number greater than 1)\n"))
    
    while not guessed_right:
        ai_guess = random.randint(lowest, highest)
        guess = input(f"How about {ai_guess}? \nhigh / low / right\n")
        if guess == "high":
            highest = ai_guess
            print("Too high? Ok...\n")
            guess_count += 1
        elif guess == "low":
            lowest = ai_guess
            print("Too low? Ok...\n")
            guess_count += 1
        elif guess == "right":
            print("I got it? Hooray!")
            guessed_right = True
            guess_count += 1
    if guess_count > 1:
        print(f"I got the number in {guess_count} guesses.")
    else:
        print(f"I got the number in {guess_count} guess.")
    check_again()


def check_again():
    again = input(f"\nDo you want to play again? y/n\n")
    if again == "y":
        start()
    elif again == "n":
        end()
    else:
        print("\nThat was not a valid input")
        check_again()
        

def end():
    print("\nThank you for playing.")


start()
