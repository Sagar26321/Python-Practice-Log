def rem(l, word):
    n= []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Harry", "Sagar", "Rohan", "Anirban"]
print(rem(l,"an"))