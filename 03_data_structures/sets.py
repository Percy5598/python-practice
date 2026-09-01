skills = {"Python", "SQL", "Python", "Excel", "SQL", "Power BI"}

# Add elements to the set
skills.add("Tableau")
skills.add("Machine Learning")

# Remove elements from the set
skills.remove("Excel")  # Raises KeyError if the element is not found
skills.discard("SQL")  # Does not raise an error if the element is not found

# Check membership
print("Python" in skills)

# Set operations
python_skills = {"Python", "Pandas", "NumPy", "SQL", "Git"}
data_science_skills = {"Python", "Pandas", "Scikit-learn", "SQL", "Statistics"}
# Union
print (python_skills | data_science_skills)

# Intersection
print(python_skills & data_science_skills)

# Difference
print (python_skills - data_science_skills)

# Symmetric difference 
print (python_skills ^ data_science_skills)


print(skills)