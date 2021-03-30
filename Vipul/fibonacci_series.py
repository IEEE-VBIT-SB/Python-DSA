def fib(n):
  n1 = 0 
  n2 =1 
  for i in range(n):
    if i <= 1:
      sum = i
    else:
      sum = n1 + n2 
      n1 = n2
      n2 = sum
    print(sum, end= ' ')
