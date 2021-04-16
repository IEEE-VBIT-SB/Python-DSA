class Student:
    def __init__(self,name,rollno,attendance,due):
        self.name=name
        self.rollno=rollno
        self.attendance=attendance
        self.due=due
    
    def displayStudents(self):
        print("Name : ",self.name)
        print("Roll number :",self.rollno)
        print("Attendance :",self.attendance)
        print("Fee due :",self.due)
        print("")

Student1=Student("Srinivas",20,90,1000)
Student2=Student("XYZ",21,84,1500)
Student1.displayStudents()
Student2.displayStudents()