def speed_check():
    x=0
    d=int(input("enter the distance "))
    d=d/5
    for i in range(int(d)):
        speed=int(input("enter the speed: "))
        if speed<=70:
            print("OK")
            break
        else:
            x+=1
            print(str(x) +" demerit point")
        if x==12:
            print("your license is cancelled")
speed_check()
