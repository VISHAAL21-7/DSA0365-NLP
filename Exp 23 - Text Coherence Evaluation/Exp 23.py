text = input("Enter text: ")

sentences = [s.strip() for s in text.split(".") if s.strip()]

if len(sentences) > 1:
    print("The text is coherent.")
else:
    print("The text has low coherence.")
