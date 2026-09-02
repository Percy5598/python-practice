text = "Python is powerful"

# print the string
print(text)

# print the length of the string
print(len(text))

# print the first character of the string
print(text[0])

# print the last character of the string
print(text[-1])

# print "python" using slicing
print(text[0:6])

# replace jave with python
sentence = "I love Java. Java is easy."
new_sentence = sentence.replace("Java", "Python")
print(new_sentence)

# split the string into a list of words
skills = "Python,SQL,Machine Learning,Git,Docker"
print(skills.split(","))

# join the list
skills = ["Python", "SQL", "Git", "Docker"]
print(",".join(skills))

# checking if a string starts with a specific substring
description = "Python developer with SQL and machine learning experience"
print(description.startswith("Python"))
print("Python" in description)

# Count words in a string
text = "Python is powerful. Python is easy to learn. Python is popular."
word_count = text.count("Python")
print(f"The word 'Python' appears {word_count} times in the text.")
