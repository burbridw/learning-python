import random

options = ["rock", "paper", "scissors"]

def game_on(list):
    print("\n____________________________\n\nLet's play\n")
    player_play = input("Choose your play: (rock/paper/scissors)\n\n")
    #random_number = random.randint( 0, len(list)-1 )
    #ai_play = options[random_number]
    ai_play = random.choice(list)
    check_result(player_play, ai_play)

def check_result(player, ai):
    print("\n____________________________\n")
    if player == ai:
        print(f"\nThe AI plays {ai}\n")
        print("There is no winner\n")
        check_again()
    elif player == "rock":
        if ai == "scissors":
            print(f"\nThe AI plays {ai}\n")
            win(player, ai)
        else:
            print(f"\nThe AI plays {ai}\n")
            lose(player, ai)
    elif player == "paper":
        if ai == "rock":
            print(f"\nThe AI plays {ai}\n")
            win(player, ai)
        else:
            print(f"\nThe AI plays {ai}\n")
            lose(player, ai)
    elif player == "scissors":
        if ai == "paper":
            print(f"\nThe AI plays {ai}\n")
            win(player, ai)
        else:
            print(f"\nThe AI plays {ai}\n")
            lose(player, ai)
    else:
        print("That was not a valid choice. Try again")
        game_on(options)

def win(player, ai):
    print(f"Your {player} beats {ai}\n")
    check_again()

def lose(player, ai):
    print(f"Your {player} loses to {ai}\n")
    check_again()

def check_again():
    again = input("Do you want to play again? (y/n)\n\n")
    if again == "y":
        game_on(options)
    elif again == "n":
        end()
    else:
        print("\nPlease enter y or n\n")
        check_again()

def end():
    print("\nThank you for playing\n")

game_on(options)