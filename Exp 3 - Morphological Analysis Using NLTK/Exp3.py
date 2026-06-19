from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk

nltk.download('wordnet')

sentence = "The boys are playing games and running in the gardens ."

words = sentence.split()

ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print("{:<15}{:<15}{:<15}".format("Original Words", "Stemmed", "Lemmatized"))
print("-" * 45)

for word in words:
    stemmed = ps.stem(word)
    lemmatized = lemmatizer.lemmatize(word)
    print("{:<15}{:<15}{:<15}".format(word, stemmed, lemmatized))
