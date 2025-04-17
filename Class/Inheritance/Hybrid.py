class Person:
    def show(self):
        print("This is person class")

class Employee(Person):
    def display(self):
        print("This is Employee class")

class Manager(Employee,Person):
    def execute(self):
        print("This is Manager class")


obj=Manager()
obj.show()
obj.display()
obj.execute()