import random
from words import words

def startup(list):
    target = random.choice(list)
    guess_display = ""
    already_guessed = []
    for x in target:
        guess_display += "-"
    game_on(target, guess_display, already_guessed)


def game_on(word, display, wrong):
    while "-" in display:
        print(f"\nGuess the word\n\n{display}\n")
        if len(wrong) > 0:
            print(f"You have already tried {wrong}")
        guess = input("\nGuess a letter: ")
        if len(guess) == 1:
            if guess in word:
                count = word.count(guess)
                if count == 1:
                    index = word.index(guess)
                    display = display[:index] + guess + display[index + 1:]
                    word = word[:index]+"*"+word[index + 1:]
                    print("\nThat letter is in the word\n")
                    game_on(word, display, wrong)
                elif count > 1:
                    while count > 0:
                        print(count)
                        index = word.index(guess)
                        display = display[:index] + guess + display[index + 1:]
                        word = word[:index]+"*"+word[index + 1:]
                        count = word.count(guess)
                    print("\nThat letter is in the word\n")
                    game_on(word, display, wrong)
                    
                    
            elif not guess in word:
                print("\nThat letter is not in the word. Try again\n")
                wrong.append(guess)
                game_on(word, display, wrong)
        print("\nPlease enter only one letter\n")
    print(f"\nYou have found all the letters\n\nThe word was {display}")
    again = input("\nHit ENTER to play again")
    startup(words)
    

startup(words)
