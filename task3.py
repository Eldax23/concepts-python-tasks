
import random

words = ["apple" , "car" , "game" , "technology" , "laptop"]

selectedWord = random.choice(words)



shuffledWord = list(selectedWord)

random.shuffle(shuffledWord)

shuffledWord = ''.join(shuffledWord)

print(f"shuffled word is : {shuffledWord}")



attempts = 5

while attempts > 0:
    attempts -= 1
    guess = input("Enter your Guess: ")
    if guess == selectedWord:
        print(f"Congratulations! You guessed the correct word!")
        exit()
    else:
        print(f"Incorrect! Try again. You have {attempts} attempts left.")


print(f" 	You’re out of attempts! The correct word was: {selectedWord}")