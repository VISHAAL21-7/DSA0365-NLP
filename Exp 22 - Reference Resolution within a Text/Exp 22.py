text = input("Enter text: ")

if "He" in text:
    text = text.replace("He", "John")
if "She" in text:
    text = text.replace("She", "Mary")

print("\nResolved Text:")
print(text)
