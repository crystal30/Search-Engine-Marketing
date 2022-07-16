import numpy as np


# 欧式距离
def euclidean(u, v):
    assert len(u) == len(v)
    u_v = zip(u, v)
    new_array = [0 for _ in range(len(u))]
    for i, sub_u_v in enumerate(u_v):
        u, v = sub_u_v
        new_array[i] = np.power(u - v, 2)

    new_array = np.array(new_array)
    return np.power(np.sum(new_array), 0.5)


# 余弦距离
def cosine(u, v):
    u_array = np.array(u)
    v_array = np.array(v)

    dot_product = np.sum(u_array * v_array)
    module_u = np.power(np.sum(u_array * u_array), 0.5)
    module_v = np.power(np.sum(v_array * v_array), 0.5)

    return 1 - dot_product / (module_u * module_v)


# jaccard 距离
def jaccard(u, v):
    assert len(u) == len(v)
    c_tt = 0
    c_tf_ft = 0  # c_tf + c_ft

    u_v = zip(u, v)
    for sub_u, sub_v in u_v:
        if sub_u == 0 and sub_v == 0:
            continue
        elif sub_u == sub_v:
            c_tt += 1
        else:
            c_tf_ft += 1

    return c_tf_ft / (c_tf_ft + c_tt)


count_vector_1 = [1, 1, 2, 1, 1, 1, 0, 0, 0]
count_vector_2 = [1, 1, 1, 0, 1, 1, 1, 1, 1]

euclidean_dist = euclidean(count_vector_1, count_vector_2)
print("euclidean dist: ", euclidean_dist)

cosine_dist = cosine(count_vector_1, count_vector_2)
print("cosine dist: ", cosine_dist)

jaccard_dist = jaccard(count_vector_1, count_vector_2)
print("jaccard dist: ", jaccard_dist)
