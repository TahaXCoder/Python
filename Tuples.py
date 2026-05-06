# Ordered , unchangeable , allows duplicates . Use when data should not change.

coordinates = (30.3753, 69.3451 )# Pakistan coords

rgb = (255, 0 , 128)

# Access same as list
print(coordinates[0])    # 30.3753

# Can't modify — this will ERROR:
# coordinates[0] = 10   ❌

# Tuple unpacking
lat, lon = coordinates
print(lat)    # 30.3753

# Single item tuple needs comma
single = (42,)    # without comma it's just int