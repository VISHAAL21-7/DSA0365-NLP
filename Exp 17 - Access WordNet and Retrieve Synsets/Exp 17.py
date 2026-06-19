from nltk.corpus import wordnet

word = "bank"
for syn in wordnet.synsets(word):
    print(syn.name(), ":", syn.definition())
