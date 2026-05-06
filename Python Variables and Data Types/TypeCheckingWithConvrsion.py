x = 42
print(type(x))           # <class 'int'>
print(isinstance(x, int))   # True

# Conversion
int("42")       # str → int
float("3.14")   # str → float
str(100)        # int → str
list((1,2,3))   # tuple → list
tuple([1,2,3])  # list → tuple
set([1,1,2,3])  # list → set (removes duplicates)
