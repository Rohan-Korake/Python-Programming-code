class Calculator:
    def add(self,a=0,b=0,c=0,d=0,e=0):
        print("Addition : ",a+b+c+d)

cal=Calculator()
cal.add(10,20,30,40,50)
cal.add(10,20)
cal.add(10,20,30)
cal.add(10)