coordinates = (28.7041, 77.1025)  # latitude, longitude
print(type(coordinates))
x,y = coordinates  # unpacking the tuple
print("Target latitude:", x)
print("Target longitude:", y)

data = (10, 20, 30)
data[0] = 100  # Try to change 10 to 100
print(data)
