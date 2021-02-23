import random

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

options = [ROCK, PAPER, SCISSORS]
win_results = {ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER}

user_choice = input()
computer_choice = random.choice(options)

if win_results[user_choice] == computer_choice:
    print("Well done. The computer chose {} and failed".format(computer_choice))
elif win_results[computer_choice] == user_choice:
    print("Sorry, but computer chose {}".format(computer_choice))
else:
    print("There is a draw {}".format(computer_choice))
