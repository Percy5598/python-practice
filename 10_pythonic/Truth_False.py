# Boolean
a = bool(1)          # True
b = bool(-10)        # True
c = bool("hello")    # True
d = bool([1, 2, 3])  # True

print(a, b, c, d)

e = bool(0)       # False
f = bool("")      # False
g = bool([])      # False
h = bool({})      # False
i = bool(None)    # False

print(e, f, g, h, i)

# None 
name = None
print(name)

if name is None:
    print("No name provided")

name = "Percy"
if name is not None:
    print(name)

def find_user(users, target):
    for user in users:
        if user == target:
            return user

    return None

user = find_user(["Alice", "Bob"], "Charlie")

if user is None:
    print("User not found")


value = 0

if value is None:
    print("Missing")
else:
    print("Value exists")

# is vs ==
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   
print (a is b)

# Walrus operator := i.e., assignment 
if (length := len("Python")) > 5:
    print(length)

