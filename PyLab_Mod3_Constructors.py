#constructor

class person:
    def __init__(self):
        self.name = "Smyan"
    def printt(self):
        print(self.name)

sara = person()
sara.printt()

class add:
    first=0
    second = 0
    def __init__(self,f,s):
        self.first = f
        self.second = s
    def addthis(self):
        self.answer = self.first + self.second
    def display(self):
        print("The first number is : ", str(self.first))
        print("The second number is : ", str(self.second))
        print("The sum of these numbers is : ", str(self.answer))

sara = add(200,300)
sara.addthis()
sara.display()
