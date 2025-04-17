class Parent1:
    def show(self):
        print("This is parent1 class")

class Parent2:
    def execute(self):
        print("This is parent2 class")

class Child(Parent1,Parent2):
    def display(self):
        print("This is child class")

obj=Child()
obj.show()
obj.execute()
obj.display()