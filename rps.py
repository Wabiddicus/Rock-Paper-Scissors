import random

random_rps = random.choice(['rock', 'paper', 'scissors'])

rps = input("Enter rock, paper, or scissors: ")

if rps == random_rps:
    print("It's a tie!")

elif (rps == 'rock' and random_rps == 'scissors') or \
     (rps == 'paper' and random_rps == 'rock') or \
     (rps == 'scissors' and random_rps == 'paper'):
    print("You win!")

else:
    print("You lose!")
