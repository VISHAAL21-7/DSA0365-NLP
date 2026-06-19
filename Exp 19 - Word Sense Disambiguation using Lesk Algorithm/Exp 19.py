import nltk
from nltk.wsd import lesk

nltk.download('wordnet')
nltk.download('omw-1.4')

sentence = input("Enter a sentence: ")
word = input("Enter the ambiguous word: ")

sense = lesk(sentence.split(), word)

if sense:
    print("Word Sense:", sense.name())
    print("Meaning:", sense.definition())
else:
    print("No sense found")
