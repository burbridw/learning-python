import random

print("Let the games commence \n")



def game_on():
    guessed_right = False
    guess = ""
    guess_count = 0
    lowest = 1
    highest = 20
    the_number = random.randint(1, 20)

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
    

def check_again():
    again = input(f"\nDo you want to play again? y/n\n")
    if again == "y":
        game_on()
    elif again == "n":
        end()
    else:
        print("\nThat was not a valid input")
        check_again()
        

def end():
    print("\nThank you for playing.")

game_on()