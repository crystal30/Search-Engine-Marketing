import sys

rawDataFile = "./RenMinData.txt"
idDataFile = "./RenMinData.id.txt"
wordDicFile = "./WordDic.rm.txt"

WordIDTable = {}

id = 1
infile = open(rawDataFile, 'r', encoding='gb2312')
s = infile.readline().strip()
while len(s) > 0:
    #s = s.decode("gb2312")
    for word in s.split(' '):
        if word not in WordIDTable:
            WordIDTable[word] = id
            id += 1
    s = infile.readline().strip()
infile.close()
print("Reading raw data file finished!")
print("Total number of words:", len(WordIDTable))

infile = open(rawDataFile, 'r', encoding='gb2312')
outfile = open(idDataFile, 'w')
s = infile.readline().strip()
while len(s) > 0:
    #s = s.decode("gb2312")
    words = s.split(' ')
    for i in range(len(words)-1):
        word = words[i]
        if word not in WordIDTable:
            print("OOV word found!")
        else:
            outfile.write(str(WordIDTable[word]))
            outfile.write(' ')
    word = words[len(words)-1]
    if word not in WordIDTable:  # 未登录词
        print("OOV word found!")
    else:
        outfile.write(str(WordIDTable[word]))
    outfile.write("\r\n")
    s = infile.readline().strip()
infile.close()
outfile.close()
print("Writing id data file finished!")

outfile = open(wordDicFile, 'w', encoding='gb2312')
for word in WordIDTable.keys():
    # outfile.write(word.encode("gb2312"))
    outfile.write(word)
    outfile.write(' ')
    outfile.write(str(WordIDTable[word]))
    outfile.write("\r\n")
outfile.close()
print("Writing word id table file finished!")
