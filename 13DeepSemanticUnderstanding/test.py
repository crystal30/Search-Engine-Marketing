import pandas as pd

from collections import defaultdict

res = defaultdict(list)
tpok_list = [(9, 1),(9, 1)]
res[0].extend(tpok_list)
res[0].extend(tpok_list)







doc_data_file = "/root/autodl-tmp/data/News2022_doc.tsv"
train_data_file = "/root/autodl-tmp/data/News2022_train.tsv"
output_data = "merge_train"
# doc_data_file = "doc_test.csv"
# train_data_file = "train_test.csv"

doc_data = pd.read_csv(doc_data_file, encoding="utf-8", sep="\t")
doc_data = doc_data.rename(columns={"qid": "docid", "docid": "doc"})
# doc_data.drop_duplicates(subset=['doc'], inplace=True)

train_data = pd.read_csv(train_data_file, encoding="utf-8", sep="\t")[["docid", "query"]]

merge_data = pd.merge(doc_data, train_data, how='right')
merge_data.dropna(inplace=True)
merge_data[["query", "doc"]].to_csv(output_data, sep="\t", header=False, index=False)

print("ok")


