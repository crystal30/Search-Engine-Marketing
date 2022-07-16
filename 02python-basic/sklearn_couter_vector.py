# --encoding=utf-8--
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "He is a boy.",
    "She is a girl, good girl."]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(X.toarray())
print("vocabulary:", vectorizer.vocabulary_)
# [[0 1 1 1 0 0 1 0 1]
#  [0 2 0 1 0 1 1 0 1]
#  [1 0 0 1 1 0 1 1 1]
#  [0 1 1 1 0 0 1 0 1]]
