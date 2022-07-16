from sklearn.feature_extraction.text import TfidfVectorizer


corpus = ['He is a boy', 'She is a girl, good girl']

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(X)
"""
  (0, 0)	0.6316672017376245 # 表示第0号句子，vocabulary中index为0的word的tfidf值
  (0, 4)	0.4494364165239821
  (0, 3)	0.6316672017376245
  (1, 2)	0.3920440146223274 # 表示第1号句子，vocabulary中index为2的word的tfidf值
  (1, 1)	0.7840880292446548
  (1, 5)	0.3920440146223274
  (1, 4)	0.2789425453258252
"""
print("tfidf\n", X.toarray())
print("feture name:", vectorizer.get_feature_names())
print("vocabulary:", vectorizer.vocabulary_)