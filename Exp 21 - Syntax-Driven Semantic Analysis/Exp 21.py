import nltk

nltk.download('averaged_perceptron_tagger_eng')

sentence = input("Enter a sentence: ")

words = sentence.split()
tags = nltk.pos_tag(words)

print("Nouns in the sentence:")

for word, tag in tags:
    if tag.startswith("NN"):
        print(word)
