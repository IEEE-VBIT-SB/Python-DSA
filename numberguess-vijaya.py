import random
randomNumber = random.randint(1,99)
guess=int(input("enter a number between 1 and 99"))
while randomNumber!=guess:
    if guess<randomNumber:
        print("Guess is too low")
        guess=int(input("enter a number between 1 and 99"))
    elif guess>randomNumber:
        print("Guess is too high")
        guess= int(input("enter a number between 1 and 99"))
print("You guesses it. Good job!")