from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "played", "runner", "running", "studies", "cats"]

print("{:<15}{:<15}".format("Word", "Stem"))
print("-" * 30)

for word in words:
    print("{:<15}{:<15}".format(word, ps.stem(word)))
