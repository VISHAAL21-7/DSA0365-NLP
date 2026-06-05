import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "NLP is very interesting"
tokens = nltk.word_tokenize(text)

print(nltk.pos_tag(tokens))