import random
from collections import defaultdict

text = "I love NLP I love machine learning I love python"

words = text.split()

bigram = defaultdict(list)

for i in range(len(words) - 1):
    bigram[words[i]].append(words[i + 1])

word = random.choice(words)
output = [word]

for i in range(10):
    if word in bigram:
        word = random.choice(bigram[word])
        output.append(word)
    else:
        break

print("Generated Text:")
print(" ".join(output))
