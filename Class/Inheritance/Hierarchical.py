
class Parent:
    def show(self):
        print("This is parent class")

class Child1(Parent):
    def execute(self):
        print("This is child1 class")

class Child2(Parent):
    def display(self):
        print("This is child2 class")

c1=Child1()
c2=Child2()
c1.show()
c1.execute()
c2.show()
c2.display()