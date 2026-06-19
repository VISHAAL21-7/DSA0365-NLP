
s = input("Enter sentence: ").split()

if (s[0].lower() == "he" and s[1].endswith("s")) or \
   (s[0].lower() in ["i", "we", "you", "they"] and not s[1].endswith("s")):
    print("Agreement Correct")
else:
    print("Agreement Incorrect")
