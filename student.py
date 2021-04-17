class Student:
    def __init__(self,name,rollno,section,fee):
        self.name=name
        self.rollno=rollno
        self.section=section
        self.fee=fee
    def display(self):
        print("Name-",self.name,"\n" "Roll no-",self.rollno,"\n" "Section-",self.section,"\n" "Fee-",self.fee,"\n")
s1=Student("harini",6,2,67000)
s2=Student("abc",3,4,13000)
s1.display()
s2.display()
