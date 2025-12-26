with open("this.txt") as f:
    content = f.read()

with open("this_copy_text", "w") as f:
    f.write(content)