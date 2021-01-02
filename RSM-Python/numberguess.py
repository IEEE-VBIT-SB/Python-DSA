import random

x=int(input("Enter lower range"))
y=int(input("Enter upper range"))
tries=y-x-1
chances=str(tries+1)
random_value= random.randint(x,y)

print('You have '+chances+' tries')
guess=int(input("Enter your guess"))

while(tries>0):
    if(guess==random_value):
        print('Guessed Correctly')
        break
    else:
        guess=int(input('Wrong guess. Try Again: '))
        tries=tries-1

if(tries==0):
    if(guess==random_value):
        print('Guessed Correctly')
    else:
        print('Wrong guess. No lives left')