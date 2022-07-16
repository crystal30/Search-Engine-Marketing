# capus = ['He is a boy',
#         'She is a girl, good girl']

capus = ['这只 皮靴 号码 大了 那只 号码 合适',
         '这只 皮靴 号码 不小 那只 更 合适' ]
word_set = set()
for text in capus:
    for word in text.strip().split(" "):
        word_set.add(word.strip(','))

print("语料库 word", word_set)

# 带index的语料库的
index_word = dict()
for index, word in enumerate(word_set):
    index_word[word] = index

print("语料库index_word", index_word)


# 得到count vector
text_count = []
for text in capus:
    count_list = [0 for _ in range(len(word_set))]
    for word in text.strip().split(" "):
        count_list[index_word[word.strip(',')]] += 1
    
    text_count.append(count_list)

print("count vector", text_count)
