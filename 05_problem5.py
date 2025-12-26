words =["Donkey", "banana", "Monkey"]

with open("file.txt", "r") as f:
    content = f.read()

for word in words:
 content = content.replace(word,"#" * len(words))

with open("file.txt", "w") as f:
    f.write(content)

    