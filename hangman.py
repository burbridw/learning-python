import random
from words import words

target = random.choice(words)

guess_display = ""

print(target)
print(len(target))
num = 1

for x in target:
    
    guess_display += " " + str(num) + " "
    num += 1


def game_on(word, display):
    correct_guesses = 0
    print(f"\nGuess the word\n\n{display}\n")
    guess = input("\nGuess a letter: ")
    if guess in word:
        count = word.count(guess)
        print(word.index(guess))
        if count == 1:
            index = word.index(guess)
            print(display[:index])
            print(display[index+1:])
            print(display)
            display1 = display[:index]
            display2 = display[index + 1:]
            display = display1 + f" {guess} " + display2
            print(display)







game_on(target, guess_display)
