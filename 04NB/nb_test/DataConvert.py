import sys
import os
import random

WordList = []
WordIDDic = {}
TrainingPercent = 0.8

# inpath = sys.argv[1]
# OutFileName = sys.argv[2]
inpath = "data/"
OutFileName = "nb_data"

trainOutFile = open(OutFileName+".train", "w")
testOutFile = open(OutFileName+".test", "w")

def ConvertData():
    i = 0
    tag = 0
    for filename in os.listdir(inpath):
        # 挑选出 大类为 business， auto， sport 的文章，并标注tag
        if filename.find("business") != -1:
            tag = 1
        elif filename.find("auto") != -1:
            tag = 2
        elif filename.find("sport") != -1:
            tag = 3
        i += 1

        # 分测试集和训练集
        rd = random.random()
        outfile = testOutFile
        if rd < TrainingPercent:
            outfile = trainOutFile

        if i % 100 == 0:
            print(i,"files processed!\r")

        # 打开文件
        infile = open(os.path.join(inpath, filename), 'r', encoding='utf-8')
        outfile.write(str(tag)+" ")  # 将file 的 flag 写入到outfile中
        content = infile.read().strip()
        #content = content.decode("utf-8", 'ignore')
        # 将文章分为一个一个的单词，并将单词转换为id
        words = content.replace('\n', ' ').split(' ')
        for word in words:
            if len(word.strip()) < 1:
                continue
            if word not in WordIDDic:
                WordList.append(word)
                WordIDDic[word] = len(WordList)
            outfile.write(str(WordIDDic[word])+" ")
        outfile.write("#"+filename+"\n")
        infile.close()

    print(i, "files loaded!")
    print(len(WordList), "unique words found!")

ConvertData()
trainOutFile.close()
testOutFile.close()