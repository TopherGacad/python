#simple error handling
import sys #to import system module

#ZeroDivisionError:
x = int(input("Enter x: "))
y = int(input("Enter y: "))

try:
    result = x/y
except ZeroDivisionError:
    print("Error: Cannot divide by 0")
    sys.exit(1) #allow the system to exit the program
except ValueError:
    print("Error: Enter a number only")
    sys.exit(1)

print(f"{x} / {y} = {result}")