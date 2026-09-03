# Create a file named "notes.txt" inside "python-practice/06_files" and write the text "I am learning Python." into it.

with open("python-practice/06_files/notes.txt", "w") as file:
    file.write("I am learning Python.")     

# Read the contents of the "notes.txt" file and print it to the console.
with open("python-practice/06_files/notes.txt", "r") as file:
    content = file.read()
    print(content)  

# Append to file
with open("python-practice/06_files/notes.txt", "a") as file:
    file.write("\nI am practicing file handling.")

# Read line by line and print each line to the console.
with open("python-practice/06_files/notes.txt", "r") as file:
    for line in file:
        print(line.strip())