import random

while True:

    random_rps = random.choice(['rock', 'paper', 'scissors'])
    rps = input("Enter rock, paper, or scissors or q to quit): ").lower()

    if rps == 'q':
        print("thanks for playing!")
        break

    if rps not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue

    if rps == random_rps:
        print("It's a tie!")

    elif (rps == 'rock' and random_rps == 'scissors') or \
        (rps == 'paper' and random_rps == 'rock') or \
        (rps == 'scissors' and random_rps == 'paper'):
        print("You win!")

    else:
        print("You lose!")
        print("The computer chose:", random_rps)
        print("You chose:", rps)
        print("Better luck next time!")
