import sys
import math

current_word = None
count = 0

docs_cnt = 508

for line in sys.stdin:
    ss = line.strip().split('\t')
    if len(ss) != 2:
        continue

    word, val = ss
    if current_word == None:
        current_word = word

    if current_word != word:
        idf = math.log(float(docs_cnt) / (float(count) + 1.0))
        print('\t'.join([current_word, str(idf)]))
        current_word = word
        count = 0


    count += int(val)

idf = math.log(float(docs_cnt) / (float(count) + 1.0))
print('\t'.join([current_word, str(idf)]))
