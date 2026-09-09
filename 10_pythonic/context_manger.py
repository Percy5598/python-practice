"""
with open("data.txt", "r") as file:
    data = file.read()


open resource
     ↓
use resource
     ↓
automatically clean up    

file = open("data.txt", "r")
data = file.read()
file.close()

with something() as resource:
    use(resource)

with database_connection() as connection:
    ...

Special methods
__enter__()
__exit__()  

with resource as x:
    do_something()


   x = resource.__enter__()

try:
    do_something()
finally:
    resource.__exit__() 

"""

