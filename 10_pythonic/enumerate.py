"""
Non Pythonic
names = ["Alice", "Bob", "Charlie"]

for i in range(len(names)):
    print(i, names[i])

Prefer 
for index, value in enumerate(values):

Instead of 
for index in range(len(values)):
    value = values[index]        
"""
names = ["Alice", "Bob", "Charlie"]

for i, name in enumerate(names):
    print(i, name)


for i, name in enumerate(names, start=1):
    print(i, name)    