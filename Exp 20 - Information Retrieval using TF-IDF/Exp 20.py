from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "Python is easy to learn",
    "Python is used in machine learning",
    "Machine learning is a popular field"
]

tfidf = TfidfVectorizer()
matrix = tfidf.fit_transform(docs)

print("TF-IDF Matrix:")
print(matrix.toarray())
