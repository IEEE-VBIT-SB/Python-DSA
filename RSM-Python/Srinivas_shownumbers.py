def showNumbers(limit):
    for i in range (0,limit+1):
        if(i%2==0):
            print(str(i)+' EVEN')
        else:
            print(str(i)+' ODD')

limit=int(input('Enter the limit'))
showNumbers(limit)
