#6. guess a number between 1 and 9
import random
num = random.randint(1, 9)
while True:
    guess = int(input("Guess the number (1-9): "))
    if guess == num:
        print("Well guessed!")
        break
