#inheritance

class person:
    def __init__(self,firstname,lname):
        self.name=firstname
        self.last=lname
    def printname(self):
        print(self.name,self.last)

class student(person):
    graduation = 2024
    def __init__(self,firstname,lname):
        super().__init__(firstname,lname)
    def printgrad(self):
        print("The Graduation year is : ", self.graduation)
class employee(person):
    pass

sara = student("Smyan","Mangot")
sara.printname()
sara.printgrad()
