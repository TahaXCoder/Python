is_student = True
is_graduated = False

# Comparison Operators → return bool
print(10 > 5)     # True
print(10 == 5)    # False
print(10 != 5)    # True

# Logical Operators
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# Truthy / Falsy values
print(bool(0))       # False
print(bool(""))      # False
print(bool(None))    # False
print(bool(1))       # True
print(bool("hi"))    # True
print(bool([]))      # False  ← empty list