import random
game = ['scissors','rock','paper']
win_cases = {'rock':'scissors','paper':'rock','scissors':'paper'}
while True:
  user_input = input('enter your choice :')
  if user_input =="exit":
      print('Bye!')
      break
  elif user_input not in game:
        print("Invalid input")
        continue
  com_choice = random.choice(game)
  if win_cases[user_input] == com_choice:
      print('Well done. The computer chose {} and failed'.format(com_choice))
  elif win_cases[com_choice] == user_input:
       print('Sorry, but the computer chose {}'.format(com_choice))
  else:
      print('There is a draw ({})',format(user_input))
     
