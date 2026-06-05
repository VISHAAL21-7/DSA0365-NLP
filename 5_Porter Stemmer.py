from nltk.stem import PorterStemmer

ps = PorterStemmer()
words = ["luther", "flies", "happiness"]

for word in words:
    print(word, "->", ps.stem(word))