"""
Non Pythonic
names = ["Alice", "Bob", "Charlie"]

for i in range(len(names)):
    print(i, names[i])
"""
names = ["Alice", "Bob", "Charlie"]

for i, name in enumerate(names):
    print(i, name)


for i, name in enumerate(names, start=1):
    print(i, name)    