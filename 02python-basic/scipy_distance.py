from scipy.spatial.distance import euclidean, cosine, jaccard

count_vector_1 = [1, 1, 2, 1, 1, 1, 0, 0, 0]
count_vector_2 = [1, 1, 1, 0, 1, 1, 1, 1, 1]

euclidean_dist = euclidean(count_vector_1, count_vector_2)
print("euclidean dist: ", euclidean_dist)

cosine_dist =cosine(count_vector_1, count_vector_2)
print("cosine dist: ", cosine_dist)

jaccard_dist =jaccard(count_vector_1, count_vector_2)
print("jaccard dist: ", jaccard_dist)
