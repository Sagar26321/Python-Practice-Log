# f = open("my.txt")
# print(f.read())
# f.close()

# The same above can be written using with statement like this :
with open("my.txt") as f:
    print(f.read())

# you dont have to explicitly close the file i.e no need for writing f.close()