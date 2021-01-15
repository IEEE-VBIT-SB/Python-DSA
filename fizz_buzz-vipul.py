def fizz_buzz(x):
    if x%3==0 and x%5==0:
        print("Fizzbuzz")
    elif x%5==0:
        print("buzz")
    elif x%3==0:
        print("Fizz")
    else:
        print(x)
fizz_buzz(4)
