def getsum(limit):
    x=0
    for i in range(limit+1):
        if i%3==0 or i%5==0:
            x=x+i
    return x
sum=getsum(10)
print(sum)
