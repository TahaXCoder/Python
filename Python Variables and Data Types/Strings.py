name = "Taha"
uni = 'COMSATS'
multi = """This is
multi-line string"""

# String Operations
print(len(name))          # 4 — length
print(name.upper())       # TAHA
print(name.lower())       # taha
print(name[0])            # T — indexing
print(name[-1])           # a — negative index
print(name[1:3])          # ah — slicing

# F-strings (most used)
age = 20
print(f"My name is {name} and I am {age} years old")

# Useful Methods
text = "  hello world  "
print(text.strip())           # remove spaces
print(text.replace("hello", "hi"))
print("hello world".split(" "))   # ['hello', 'world']
print("Taha".startswith("T"))     # True