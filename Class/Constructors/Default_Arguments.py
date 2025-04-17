class User:
    def __init__(self,name="Unknown"):
        self.Name=name
        print("This is Default Arguments constructor....")
        print("Name : ",self.Name)

obj=User()
