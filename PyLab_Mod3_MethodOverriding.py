#polymorphism2

class parent():
    def __init__(self):
        self.value = "Hi from Parent"
    def show(self):
        print(self.value)

class child(parent):
    def __init__(self):
        self.value = "Hi from Child"
    def show(self):
        print(self.value)

rajiv = parent()
sara = child()

rajiv.show()
sara.show()
        
