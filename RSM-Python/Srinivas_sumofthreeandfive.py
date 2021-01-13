def sumofmul(limit):
    sumoff=0
    sumoft=0
    for i in range(0,limit+1):
        if(i%3==0):
            sumoft=sumoft+i
        elif(i%5==0):
            sumoff=sumoff+i
    answer=sumoft+sumoff
    return(answer)

limit=int(input('Enter the limit'))
answer=sumofmul(limit)
print(answer)