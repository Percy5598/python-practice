# value error
# number = int("hello") 

# syntax error
# if x > 5
   # print (x)

#  Exceptions 
# x = 10 / 0  

# Other errors are ValueError, TypeError, IndexError, KeyError, AttributeError, ImportError, ModuleNotFoundError, FileNotFoundError, ZeroDivisionError, NameError, and many more.

# Complete try and except block
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print(f"Result: {result}")

finally:
    print("Done.")

