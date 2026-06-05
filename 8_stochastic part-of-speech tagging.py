from collections import defaultdict

training_data = [("dog", "NN"), ("barks", "VB"),
                 ("cat", "NN"), ("runs", "VB")]

prob = defaultdict(lambda: defaultdict(int))

for word, tag in training_data:
    prob[word][tag] += 1

def stochastic_tag(word):
    tags = prob[word]
    return max(tags, key=tags.get) if tags else "NN"

print(stochastic_tag("dog"))