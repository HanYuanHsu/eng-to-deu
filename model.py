import os
import openai

import math
import torch
from torch import nn, Tensor
from torch.nn import TransformerEncoder, TransformerEncoderLayer
from torch.utils.data import dataset

MAX_LEN = 20000 # the maximal number of characters that a sentence can have as the input of
# the transformer model

class NoKeyError(Exception):
    pass

api_key = os.getenv("OPENAI_API_KEY", "")
if api_key != "":
    openai.api_key = api_key
else:
    raise NoKeyError("OPENAI_API_KEY is not set")

ROLE_DESCRIPTION = "You are a native English and German speaker. Given the English sentence, translate it into German."

def gpt_eng_to_deu(eng_sentence): 

    msg=[
        {"role": "system", "content": ROLE_DESCRIPTION},
        {"role": "user", "content": "Good Morning!"},
        {"role": "assistant", "content": "Guten Morgen!"},
        {"role": "user", "content": "Good Morning! What are your plans today?"},
        {"role": "assistant", "content": "Guten Morgen! Was sind deine Pläne für heute?"},
        {"role": "user", "content": eng_sentence}
    ]
    
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=msg,
      temperature=0
    )


    return response.choices[0]['message']['content']


# https://pytorch.org/tutorials/beginner/transformer_tutorial.html
class PositionalEncoding(nn.Module):
    def __init__(self, d_model: int, dropout: float = 0.1, max_len: int = MAX_LEN):
        # d_model: the embedding dimension 
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)

        position = torch.arange(max_len).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2) * (-math.log(10000.0) / d_model))
        pe = torch.zeros(max_len, 1, d_model)
        pe[:, 0, 0::2] = torch.sin(position * div_term) # 0::2 means step size = 2
        pe[:, 0, 1::2] = torch.cos(position * div_term) # the sines and cosines are alternating
        # recall the postional embedding formulas in the CS 182 slides
        self.register_buffer('pe', pe)

    def forward(self, x: Tensor) -> Tensor:
        """
        Arguments:
            x: Tensor, shape ``[seq_len, batch_size, embedding_dim]``
        """
        seq_len = x.size(0) 
        assert seq_len <= MAX_LEN

        x = x + self.pe[:seq_len] # :seq_len is a slicing operation that selects the first 5 elements along the first dimension of the tensor.
        return self.dropout(x)
    



#######################
if __name__ == '__main__':
    seq_len = 100
    batch_size = 32
    embedding_dim = 128
    x = torch.randint(0, 128, size=(seq_len, batch_size, embedding_dim))
    pe = PositionalEncoding(d_model=embedding_dim)
    print(pe(x).shape)


