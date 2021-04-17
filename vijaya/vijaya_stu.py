class Student:
    def __init__(self,sname,sno,sage,sfee):
        self.sname=sname
        self.sno=sno
        self.sage=sage
        self.sfee=sfee
    def display(self):
        print("Name-",self.sname,"\n" "Roll no-",self.sno,"\n" "Age-",self.sage,"\n" "Fee-",self.sfee,"\n")
s1=Student("vijaya",43,20,67000)
s2=Student("abc",36,40,35000)
s1.display()
s2.display()
