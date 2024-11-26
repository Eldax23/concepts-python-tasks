

import random

words = ["phone" , "car" , "laptop" , "notepad" , "apple"]

selectedWord = random.choice(words)


shuffledWord = list(selectedWord)

random.shuffle(shuffledWord)

shuffledWord = ''.join(shuffledWord)

print(f"the shuffled word is : {shuffledWord}")

attempts = 4

while attempts >= 0: 

    guess = input("Enter your guess : ")
    if guess == selectedWord:
        print("Congratulations! You guessed the correct word!")
        exit()
    else:
        print(f"Incorrect! Try again. You have {attempts} attempts left.")
        
    attempts -= 1


print(f" 	Youre out of attempts! The correct word was: {selectedWord}")
