words = ["I", "am", "running", "to", "school"]

tags = ["NN", "NN", "NN", "NN", "NN"]

for i in range(len(words)):
    if words[i].endswith("ing"):
        tags[i] = "VBG"
    elif words[i].lower() in ["am", "is", "are"]:
        tags[i] = "VB"
    elif words[i].lower() in ["to"]:
        tags[i] = "TO"
    elif words[i].lower() == "i":
        tags[i] = "PRP"

print("{:<15}{:<10}".format("Word", "POS Tag"))
print("-" * 25)

for word, tag in zip(words, tags):
    print("{:<15}{:<10}".format(word, tag))
