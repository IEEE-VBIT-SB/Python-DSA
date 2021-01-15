def getprime(limit):
    k=0
    for i in range(limit):
         i+=1
         for z in range(i):
            if i%(z+1)==0:
                k+=1
         if k==2:
            print(i)
         k=0
getprime(20)
