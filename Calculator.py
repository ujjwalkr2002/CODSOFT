def add (x,y):
    return x + y 

def subtract (x,y):
    return x -  y 

def multiply (x,y):
    return x * y 

def divide (x,y):
    if y != 0:
        return x / y
    else:
         return "Division bty zero"


def calculator (operator, x, y):
    operations = {
        "1" : add,
        "2" : subtract,
        "3" : multiply,
        "4" : divide 
    }
    return operations[operator](x, y)

print("Select option:")
print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Divide")
operation = input("Enter the option: ")

if operation in ("1", "2", "3", "4"):
    num1  = float(input("Enter first number: "))
    num2  = float(input("Enter the second number: "))

    result = calculator(operation, num1, num2)
    print("The result is: ",result)

else:
    print("Invalid input")   