import math
from collections import OrderedDict

capus = ['He is a boy', 'She is a girl, good girl']

# 文档数量
n = len(capus)

textA = capus[0].strip().split(' ')
textA = [e.strip(',') for e in textA]

textB = capus[1].strip().split(' ')
textB = [e.strip(',') for e in textB]

# 语料库
capus_set = set(textA).union(set(textB))
print("语料库", capus_set)

# 语料库的长度
capus_n = len(capus_set)

# 带index的语料库，word为key，index为value
capus_index = dict()
for index, word in enumerate(capus_set):
    capus_index[word] = index

print("index 语料库", capus_index)

# inverse_capus_index,带index的语料库,index为key, word为value
inverse_capus_index = dict()
for index, word in inverse_capus_index.items():
    inverse_capus_index[index] = word


# 计算term frequency
def tf(text_list):
    """
    text: list
    """
    tf_list = [0 for _ in range(len(capus_set))]
    # 文档总词数
    len_text = len(text_list)
    for word in text_list:
        tf_list[capus_index[word.strip(',')]] += 1

    tf_list = [e / len_text for e in tf_list]
    return tf_list


# 打印textA的tf，textB的tf
tf_textA = tf(textA)
print("tf_textA", tf_textA)
tf_textB = tf(textB)
print("tf_textB", tf_textB)


# 计算inverse document frequency
def idf(capus):
    text_list = []
    for text in capus:
        word_list = text.strip().split(' ')
        word_set = set(e.strip(',') for e in word_list)
        text_list.append(word_set)

    print("text_list", text_list)

    idf_dict = dict.fromkeys(capus_set, 0)
    idf_list = [0 for _ in range(len(idf_dict))]
    for text in text_list:
        for word in text:
            idf_dict[word] += 1
    print("idf_dict", idf_dict)

    for word in idf_dict.keys():
        idf_list[capus_index[word]] = math.log10(n / (idf_dict[word] + 1))
        # idf_list[capus_index[word]] = math.log10(n / (idf_dict[word]))

    return idf_list


idf_list = idf(capus)
print("idf_dict ", idf_list)


# 计算tf-idf
def tf_idf(texts):
    """
    texts：list，其中的元素也是list
    """
    tf_idf_list = []
    for text in texts:
        tf_text = tf(text)
        tf_idf_text = [0 for _ in range(capus_n)]
        for i in range(capus_n):
            tf_idf_text[i] = tf_text[i] * idf_list[i]
        tf_idf_list.append(tf_idf_text)

    return tf_idf_list


tf_idf_list = tf_idf([textA, textB])
print(tf_idf_list)
