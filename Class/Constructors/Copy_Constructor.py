class Proxy:
    def __init__(self,val):
        self.Value= val

    def dispaly(self):
        print("This is Copy Constructor")
        print("Value : ",self.Value)

obj1=Proxy(17)
obj2=Proxy(obj1.Value)
obj2.dispaly()