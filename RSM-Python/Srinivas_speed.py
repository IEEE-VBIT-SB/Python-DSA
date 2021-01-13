speed=int(input('Enter Speed'))

def checker(speed):
    if(speed<70):
        print('OK')
    else:
        newspeed=int(speed-70)
        demerit=newspeed/5
        return demerit

demerit = checker(speed)

print('Points:'+str(demerit))

if(demerit>=12):
    print('Licence Suspended')
