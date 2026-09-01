students = ["Anna", "Mika", "John", "Sara", "David"]

for names in students:
    print(names)


# Adding and inserting elements in list
students.append("Emily")  # Add to the end of the list
students.insert(2, "Michael")  # Insert at index 2

 # Lets practice indexing in list 
print (students[0], students[-1], students[2], students[4:])


# Lets remove elements from list
students.remove("John")  # Remove by value
del students[1]  # Remove by index  
