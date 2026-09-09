python_skills = {"Python", "SQL", "Git", "Pandas"}
job_skills = {"Python", "SQL", "Docker", "AWS"}

# Intersection
common = python_skills & job_skills
print(common)

# Difference
missing = job_skills - python_skills
print(missing)

# Union
all_skills = python_skills | job_skills
print(all_skills)

# Subset
required = {"Python", "SQL"}
print(required <= python_skills)