#simple error handling
import sys #to import system module

x = int(input("Enter x: "))
y = int(input("Enter y: "))

try:
    result = x/y
except ZeroDivisionError:
    print("Error cannot divide by 0")
    sys.exit(1) #allow the system to exit the program

print(f"{x} / {y} = {result}")