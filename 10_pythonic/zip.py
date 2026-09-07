names = ["Alice", "Bob", "Charlie"]
scores = [85, 72, 91]

# You could do this 
for i in range(len(names)):
    print(names[i], scores[i])


# Zip is alternative
for name, score in zip(names, scores):
    print(name, score)  


actual = [1, 0, 1, 1, 0]
predicted = [1, 0, 0, 1, 0]

for y_true, y_pred in zip(actual, predicted):
    print(y_true, y_pred)

for y_true, y_pred in zip(actual, predicted):
    print(y_true == y_pred)  


names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]
scores = [85, 72, 91]

for name, age, score in zip(names, ages, scores):
    print(name, age, score)  

features = ["age", "income", "score"]
values = [25, 50000, 720]

data = dict(zip(features, values))

print(data)   