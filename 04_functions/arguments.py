# Basic arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")   

introduce("Prashant", 28)

# Returnng values
def add_numbers(a, b):
    return a + b    

added_value = add_numbers(5, 10)
print(f"The sum is: {added_value}")

# Multiple arguements
def calculate_salary (monthly_salary, tax_rate):
    tax_amount = monthly_salary * tax_rate / 100
    net_salary = monthly_salary - tax_amount
    return net_salary   

salary = calculate_salary(3000, 10)
print(salary)

#Default arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Prashant")  # Uses default greeting
greet("Mika", "Hi")  # Uses custom greeting


# POsitional and keyword arguments
def display_info(name, age, country):
    print(f"Name: {name}, Age: {age}, Country: {country}")

display_info("Prashant", 28, "Finland")  # Positional arguments
display_info(age=28, name="Prashant", country="Finland")  #Keyword arguments    

# *args usecase
def calculate_average(*args):
    total = sum(args)
    count = len(args)
    return total / count if count > 0 else 0

print(calculate_average(10, 20, 30, 40, 50))

# **kwargs usecase
def display_student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_student_info(name="Prashant", age=28, country="Finland", score=85)  


# Combine everything
def analyze_student(name, *scores, **details):
    average_score = sum(scores) / len(scores) if scores else 0
    print(f"Student Name: {name}")
    print(f"Average Score: {average_score:.2f}")
    for key, value in details.items():
        print(f"{key}: {value}") 

analyze_student("Prashant", 85, 90, 78, age=28, country="Finland", major="Computer Science")

