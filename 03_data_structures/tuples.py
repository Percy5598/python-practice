student = ("Prashant", 30, "Finland", 85)

# Printing the entire tuple
print(student)

# Negative indexing
print(student[-1])  # Accessing the last element
 
# Slicing the tuple
print(student[1:3])  # Accessing elements from index 1 to 2

# Tuple unpacking
name, age, country, score = student
print(f"Name: {name}, Age: {age}, Country: {country}, Score: {score}")
 
# Using for loop to iterate through the tuple
for item in student:
    print(item)

# Tuples of Tuples
students = (
    ("Anna", 85),
    ("Mika", 92),
    ("John", 78),
    ("Sara", 95)
)

# Find the student with the highest score
highest_score_student = max(students, key=lambda x: x[1])
print(f"Student with the highest score: {highest_score_student[0]} with a score of {highest_score_student[1]}")
     