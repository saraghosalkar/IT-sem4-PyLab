#polymorphism1

class student:
    def studentclass(self, s_class = None):
        if s_class is not None:
            print("Hello ", s_class)
        else:
            print("Hi")

sara = student()
sara.studentclass()
sara.studentclass("Atharva(C2)")
