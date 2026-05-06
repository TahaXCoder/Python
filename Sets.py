#Unordered, no duplicates. Great for unique values.

skills = {"Python", "Flutter", "Java", "Python"}  # duplicate removed
print(skills)    # {'Python', 'Flutter', 'Java'}

skills.add("C++")
skills.remove("Java")

# Set Operations — very useful
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)    # union        → {1,2,3,4,5,6}
print(a & b)    # intersection → {3,4}
print(a - b)    # difference   → {1,2}
