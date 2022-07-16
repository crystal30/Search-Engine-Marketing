import sys
import os
import random
import jieba

WordList = []
WordIDDic = {}  # key is word, value is wordID

# get train and test data path
inpath = sys.argv[1]
# inpath = "data"
trainInPath = os.path.join(inpath, "training")
testInPath = os.path.join(inpath, "test")
OutFileName = sys.argv[2]
# OutFileName = "nb_data"
# set output train and test data
trainOutFileName = "%s.train" % OutFileName
testOutFileName = "%s.test" % OutFileName


def ConvertData():
    for inpath, outpath in zip([trainInPath, testInPath], [trainOutFileName, testOutFileName]):
        i = 0
        outfile = open(outpath, "w", encoding='utf-8')
        for filename in os.listdir(inpath):
            tag, _ = filename.split("_")
            i += 1
            infilePath = os.path.join(inpath, filename)
            infile = open(infilePath, 'r', encoding='utf-8')
            outfile.write(str(tag) + " ")
            content = infile.read().strip()
            # content = content.decode("utf-8", 'ignore')
            words = jieba.cut(content.replace('\n', ' '))
            # words = content.replace('\n', ' ').split(' ')
            for word in words:
                word = word.strip()
                if len(word) < 1:
                    continue
                if len(word) == 1:
                    if (33 <= ord(word) <= 47) or (58 <= ord(word) <= 64) or \
                            (91 <= ord(word) <= 96) or (123 <= ord(word) <= 126):
                        continue
                if word not in WordIDDic:
                    WordList.append(word)
                    WordIDDic[word] = len(WordList)
                outfile.write(str(WordIDDic[word]) + " ")
            outfile.write("#" + filename + "\n")
            infile.close()
            print(i, "files loaded!")
        outfile.close()

    print(len(WordList), "unique words found!")


ConvertData()
