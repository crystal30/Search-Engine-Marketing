import torch.nn as nn
from .token import TokenEmbedding
from .position import PositionalEmbedding
from .segment import SegmentEmbedding


class BERTEmbedding(nn.Module):
    """
    BERT Embedding which is consisted with under features
        1. TokenEmbedding : normal embedding matrix
        2. PositionalEmbedding : adding positional information using sin, cos
        2. SegmentEmbedding : adding sentence segment info, (sent_A:1, sent_B:2)

        sum of all these features are output of BERTEmbedding
    """

    def __init__(self, vocab_size, embed_size, dropout=0.1):
        """
        :param vocab_size: total vocab size
        :param embed_size: embedding size of token embedding
        :param dropout: dropout rate
        """
        super().__init__()
        self.token = TokenEmbedding(vocab_size=vocab_size, embed_size=embed_size)  # 2674, 256
        self.position = PositionalEmbedding(d_model=self.token.embedding_dim)  # 1, 512, 256
        self.segment = SegmentEmbedding(embed_size=self.token.embedding_dim)  # 3, 256
        self.dropout = nn.Dropout(p=dropout)
        self.embed_size = embed_size
    # x, segment_info
    def forward(self, sequence, segment_label):
        x_token = self.token(sequence)
        x_position = self.position(sequence)
        x_segment = self.segment(segment_label)
        x = self.token(sequence) + self.position(sequence) + self.segment(segment_label)
        return self.dropout(x)
