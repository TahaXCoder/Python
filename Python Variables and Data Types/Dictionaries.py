# it provide Key-value pairs . Like a real dictionary  and lookup by key

student = {
    "name": "Taha",
    "roll":"SP24-BSE-002",
    "uni":"COMSATS",
    "cgpa": 3.1
} 

# Accessing the dictionary
print(student["name"]) #Taha
print(student["roll"]) # SP24-BSE-002

#Modify

student["cgpa"] =3.5 #update
student["city"] = "Multan" # add new key

# Delete
del student["city"]
student.pop("cgpa")

# Looping
for key, value in student.items():
    print(f"{key}: {value}")

# Useful Methods
print(student.keys())
print(student.values())
print("name" in student)    # True — check if key exists