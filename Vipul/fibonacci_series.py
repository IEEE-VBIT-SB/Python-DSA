def fib(x):
    n1 = 0 
    n2 =1 
    if x == 0 :
        print("Invalid input")
    else:
        for i in range(x):
           if i <= 1:
             sum = i
           else:
             sum = n1 + n2 
             n1 = n2
             n2 = sum
           print(sum, end= ' ')
