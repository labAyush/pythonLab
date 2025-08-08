#9. rock paper scissors game
while True:
    user = input("Enter rock, paper or scissors (or 'n' to quit): ")
    if user == 'n':
        break
    import random
    computer = random.choice(["rock", "paper", "scissors"])
    print("Computer chose:", computer)
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")
