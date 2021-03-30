def fibonacci(n):
    if(n<=0):
        print("Not possible")
    elif(n==1):
        print(0)
    else:
        n1=0
        n2=1
        count=0
        while count<n:
            print(n1)
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1
