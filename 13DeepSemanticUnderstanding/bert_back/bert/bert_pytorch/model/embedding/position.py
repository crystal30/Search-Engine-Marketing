import torch.nn as nn
import torch
import math


class PositionalEmbedding(nn.Module):

    def __init__(self, d_model, max_len=512):
        super().__init__()

        # Compute the positional encodings once in log space.
        pe = torch.zeros(max_len, d_model).float()
        pe.require_grad = False
        # max_len 为512，在这里表示什么意思呢？
        # position [512, 1], div_term [128], position*div_term [512, 128]
        position = torch.arange(0, max_len).float().unsqueeze(1)
        div_term = (torch.arange(0, d_model, 2).float() * -(math.log(10000.0) / d_model)).exp()
        # 从第0列到最后一列，每隔2列填充，也就是说偶数列填充 sin(position * div_term)
        pe[:, 0::2] = torch.sin(position * div_term)
        # 从第1列到最后一列，每隔2列填充, 也就是说奇数列填充 cos(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)

        pe = pe.unsqueeze(0)
        self.register_buffer('pe', pe)

    def forward(self, x):
        return self.pe[:, :x.size(1)]
