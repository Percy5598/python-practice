students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 91}
]
students_sorted = sorted(
    students,
    key=lambda student: student["score"],
    reverse = True
)
print(students_sorted)

names = ["Bob", "Alexander", "Tom", "John"]

print(sorted(names, key=len))

# In ML
models = [
    {"model": "Linear Regression", "rmse": 4.2},
    {"model": "Random Forest", "rmse": 2.8},
    {"model": "SVM", "rmse": 3.5}
]

best = sorted(models, key=lambda x: x["rmse"])
print(best)