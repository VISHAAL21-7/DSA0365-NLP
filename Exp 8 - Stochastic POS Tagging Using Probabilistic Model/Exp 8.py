from collections import defaultdict, Counter

training_data = [
    ("I", "PRON"), ("love", "VERB"), ("NLP", "NOUN"),
    ("Python", "NOUN"), ("is", "VERB"), ("great", "ADJ")
]

word_tag_counts = defaultdict(Counter)
tag_counts = Counter()

for word, tag in training_data:
    word_tag_counts[word][tag] += 1
    tag_counts[tag] += 1

sentence = ["I", "love", "Python", "NLP"]

print("Word\tPredicted POS")
print("-" * 25)

for word in sentence:
    if word in word_tag_counts:
        tag = word_tag_counts[word].most_common(1)[0][0]
    else:
        tag = "NOUN"
    print(word, "\t", tag)
