student = {
    "name": "Prashant",
    "age": 28,
    "country": "Finland",
    "score": 85
}
# Dictionary has keys and values 
print (student["name"])  # Accessing value by key
print (student.get("age"))  # Accessing value by key using get method

# Add keys in dictionary
student["last_name"] = "Shrestha" 

# Removing a key-value pair
del student["score"]
print(student)

# check whether a key exists in the dictionary
if "country" in student:
    print("Country key exists in the dictionary.")

# lets loop through the dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Using Sum function to calculate total score of students
grades = {
    "math": 85,
    "python": 95,
    "statistics": 90,
    "machine_learning": 88
}                                                               
total_score = sum(grades.values())
max_score = max(grades.values())
print(f"Total score: {total_score}")    
print(f"Max score: {max_score}")
