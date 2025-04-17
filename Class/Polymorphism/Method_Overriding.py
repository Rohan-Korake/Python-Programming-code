class Animal:
    def Speak(self):
        print("Animal speaks")
class Dog(Animal):
    def Speak(self):
        print("Dog barks")

D=Dog()
D.Speak()