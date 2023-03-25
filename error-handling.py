#simple error handling
import sys #to import system module

#ZeroDivisionError:
try:
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
except ValueError:
    print("Error: Enter a number only")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("Error: Cannot divide by 0")
    sys.exit(1) #allow the system to exit the program


print(f"{x} / {y} = {result}")