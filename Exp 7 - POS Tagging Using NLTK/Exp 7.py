import nltk
from nltk import pos_tag

# Required downloads (run once)
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

text = "NLTK is a powerful tool for natural language processing"

words = text.split()

tags = pos_tag(words)

print("{:<20}{:<10}".format("Word", "POS Tag"))
print("-" * 30)

for word, tag in tags:
    print("{:<20}{:<10}".format(word, tag))
