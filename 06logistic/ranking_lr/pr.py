import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, average_precision_score

data = pd.read_csv('rankmodel/auc.txt')
y_score = data['pred']
y_true = data['true']

#  plot
precision, recall, thresholds = precision_recall_curve(y_true, y_score)
plt.figure("P_R curve")
plt.title("Precision/Recall Curve")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.plot(recall, precision)
plt.show()

# compute AP
AP = average_precision_score(y_true, y_score, average='macro', pos_label=1, sample_weight=None)
print("AP", AP)
