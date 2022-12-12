from os.path import join
from collections import defaultdict
from rouge import Rouge

# 指标名
metric_keys = ["main", "rouge-1", "rouge-2", "rouge-3"]

# 计算rouge用
rouge = Rouge()


def compute_rouge(source, target, unit='word'):
    """计算rouge-1、rouge-2、rouge-l
    """
    # if unit == 'word':
    #     source = remove_stopwords(source)  # 如果unit是word，则是切词
    #     target = remove_stopwords(target)
    source, target = ' '.join(source), ' '.join(target)  # 当unit设置为char时，为切字
    try:
        scores = rouge.get_scores(hyps=source, refs=target)
        return {
            'rouge-1': scores[0]['rouge-1']['f'],
            'rouge-2': scores[0]['rouge-2']['f'],
            'rouge-l': scores[0]['rouge-l']['f'],
        }
    except ValueError:
        return {
            'rouge-1': 0.0,
            'rouge-2': 0.0,
            'rouge-l': 0.0,
        }


def compute_metrics(source, target, unit='char'):
    """计算所有metrics
    """
    metrics = compute_rouge(source, target, unit)
    metrics['main'] = (
        metrics['rouge-1'] * 0.2 + metrics['rouge-2'] * 0.4 +
        metrics['rouge-l'] * 0.4
    )
    return metrics


def compute_main_metric(source, target, unit='char'):
    """
    source是原文，target是摘要内容
    计算主要metric
    """
    return compute_metrics(source, target, unit)['main']  # 取main里面的值


if __name__ == '__main__':
    data_dir = "/Users/zhao/crystal/JL/"
    save_path = "predict_result_0620_v2.tsv"
    qid_list, query_list = [], []
    with open(join(data_dir, "News2022_test.tsv"), "r", encoding="utf8") as fr:
        next(fr)
        for line in fr:
            qid, query = line.strip().split("\t")
            qid_list.append(qid)
            query_list.append(query.strip().split(" "))

    # 分批次读取新闻数据
    doc_length = 2666764  # 数据集的总长度
    # doc_batch_count = 100000  # 分为27桶
    # top_k_num = 100
    doc_batch_count = 10  # 分为27桶
    top_k_num = 5

    def read_doc():
        docid_list, doc_list = [], []
        with open(join(data_dir, "News2022_doc.tsv"), "r", encoding="utf8") as fr:
            next(fr)
            for line in fr:
                if len(doc_list) == doc_batch_count:
                    yield docid_list, doc_list
                    docid_list, doc_list = [], []
                docid, doc = line.strip().split("\t")
                doc = doc.strip().split(" ")[:512]  # 提前分词并截取最大长度
                docid_list.append(docid)
                doc_list.append(doc)
                # if len(docid_list) > 120000: break
        yield docid_list, doc_list

# 分批获取top-100，避免内存溢出, 分批次获取top100
    start = 0
    res = dict()
    doc = read_doc()
    score_list = []
    step = 0
    while start < doc_length:
        print("step ", step)
        sub_docids, sub_docs = next(doc)
        for qid_idx, i in enumerate(query_list):
            for idx, j in enumerate(sub_docs):
                score = compute_main_metric(i, j)
                score_list.append((score, idx))
            score_list.sort(key=lambda x: x[0], reverse=True)
            topk_list = score_list[:top_k_num]  # [(score, idx),(score, idx)]
            if res.get(qid_idx, None) is None:
                res[qid_idx] = topk_list
            else:
                res[qid_idx].extend(topk_list)
            # res[i].extend(topk_list)  # 先把每一个批次的100个topk加进去，最后再进行总排序
        start += 100000

    for k, v in res.items():
        v.sort(key=lambda x: x[0], reverse=True)  # 先按照分数进行排序
        res[k] = list(map(lambda x: x[1], v))[:top_k_num]  # 然后选择前一百个 id

    print("构建预测数据...")
    write_data = [
        "{}\t{}\t{}\n".format(qid, docid, rank) for qid, topk in res.items() for rank, docid in enumerate(topk, 1)]
    print("存储到本地")
    with open(save_path, "w", encoding="utf8") as fw:
        fw.writelines(write_data)












