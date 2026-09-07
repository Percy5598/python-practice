names = ["Percy", "Roy", "Jacob"]

result = {name: len(name) for name in names}

print(result)

# With conditions
scores = {
    "Alice": 85,
    "Bob": 42,
    "Charlie": 91,
    "David": 55
}

passed = {
    name: score
    for name, score in scores.items()
    if score >= 60
}
print(passed)

features = {
    "age": 25,
    "income": 50000,
    "credit_score": 720
}

scaled = {
    name: value / 100
    for name, value in features.items()
}
print(scaled)