class Student:
    def __init__(self,name,no,age,fee):
        self.name=name
        self.no=no
        self.age=age
        self.fee=fee
    def display(self):
        print("Name-",self.name,"\n" "Roll no-",self.no,"\n" "Age-",self.age,"\n" "Fee-",self.fee,"\n")
s1=Student("harini",6,19,67000)
s2=Student("abc",86,40,13000)
s1.display()
s2.display()
