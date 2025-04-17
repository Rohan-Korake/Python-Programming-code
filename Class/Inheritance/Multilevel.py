class Parent:
    def show(self):
        print("This is parent class")

class Intermediate(Parent):
    def execute(self):
        print("This is intermediate class")

class child(Intermediate):
    def display(self):
        print("This is child class")

obj=child()
obj.show()
obj.execute()
obj.display()