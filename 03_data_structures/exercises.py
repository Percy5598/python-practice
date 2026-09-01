# The program stores student, their scores, and skills in a list of dictionaries. It then prints each student's name and score, finds all unique skills among the students, identifies the highest-scoring student, and demonstrates tuple unpacking with the subject and score of the best student. 
students = [
    {
        "name": "Anna",
        "score": 85,
        "skills": {"Python", "SQL"}
    },
    {
        "name": "Mika",
        "score": 92,
        "skills": {"Python", "Git", "SQL"}
    },
    {
        "name": "Sara",
        "score": 78,
        "skills": {"Python", "Excel"}
    },
    {
        "name": "John",
        "score": 95,
        "skills": {"Python", "SQL", "Git", "Docker"}
    }
]


# 1. Print every student
print("=== STUDENTS ===")

for student in students:
    print(f"\nName: {student['name']}")
    print(f"Score: {student['score']}")

    print("Skills:")
    for skill in student["skills"]:
        print(f"  - {skill}")


# 2. Calculate average score
total_score = 0
student_count = 0

for student in students:
    total_score += student["score"]
    student_count += 1

average = total_score / student_count

print(f"\nAverage score: {average:.2f}")


# 3. Find highest-scoring student
highest = students[0]

for student in students:
    if student["score"] > highest["score"]:
        highest = student

print(f"Best student: {highest['name']}")
print(f"Best score: {highest['score']}")


# 4. Find lowest-scoring student
lowest = students[0]

for student in students:
    if student["score"] < lowest["score"]:
        lowest = student

print(f"Lowest student: {lowest['name']}")
print(f"Lowest score: {lowest['score']}")


# 5. Classify students
print("\n=== PERFORMANCE ===")

for student in students:
    score = student["score"]

    if score >= 90:
        level = "Excellent"
    elif score >= 80:
        level = "Good"
    elif score >= 70:
        level = "Pass"
    else:
        level = "Needs improvement"

    print(f"{student['name']}: {level}")


# 6. Find all unique skills
all_skills = set()

for student in students:
    for skill in student["skills"]:
        all_skills.add(skill)

print("\n=== ALL SKILLS ===")

for skill in all_skills:
    print(skill)


# 7. Count how many students have each skill
skill_counts = {}

for student in students:
    for skill in student["skills"]:

        if skill in skill_counts:
            skill_counts[skill] += 1
        else:
            skill_counts[skill] = 1

print("\n=== SKILL FREQUENCY ===")

for skill, count in skill_counts.items():
    print(f"{skill}: {count} student(s)")


# 8. Find students who know Python
print("\n=== PYTHON STUDENTS ===")

for student in students:
    if "Python" in student["skills"]:
        print(student["name"])


# 9. Create tuples containing name and score
results = []

for student in students:
    result = (student["name"], student["score"])
    results.append(result)

print("\n=== RESULTS ===")

for name, score in results:
    print(f"{name}: {score}")


# 10. Find students above average
print("\n=== ABOVE AVERAGE ===")

for student in students:
    if student["score"] > average:
        print(student["name"])
