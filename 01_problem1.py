f = open("poem.txt")
content = f.read()
if ("Twinkle" in content):
    print("The word Twinkle is present in the content.")
else:
    print("Not Here")

f.close()