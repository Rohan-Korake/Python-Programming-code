class Parent:
    def show(self):
        print("This is parent class show function")

class Child(Parent):
    def execute(self):
        print("This is child class execute functon")

obj=Child()
obj.show()
obj.execute()