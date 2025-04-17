# Global namespace
num=17

def Outside_function():
    # Enclosing namespace
    num=67

    def inside_function():
        # Local namespace
        num=100
        print("Inside function num = ",num)
    inside_function()

    print("Outside function num = ",num)
Outside_function()

print("Global num = ",num)
