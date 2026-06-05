import random
from nltk.util import bigrams

text = "I love natural language processing"
words = text.split()

bi = list(bigrams(words))
model = {}

for w1, w2 in bi:
    model.setdefault(w1, []).append(w2)

word = random.choice(words)
result = [word]

for _ in range(5):
    word = random.choice(model.get(word, words))
    result.append(word)

print("Generated Text:", " ".join(result))