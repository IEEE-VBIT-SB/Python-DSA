number=int(input('Enter a number'))
if(number%3==0):
    if(number%5==0):
        print('FizzBuzz')
    else:
        print('Fizz')

elif(number%5==0):
    print('Buzz')

else:
    print(number)