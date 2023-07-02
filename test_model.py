import torch
import math
import unittest
from utils import *

def test1():
    max_len = 50
    d_model = 128
    position = torch.arange(max_len).unsqueeze(1)
    div_term = torch.exp(torch.arange(0, d_model, 2) * (-math.log(10000.0) / d_model))
    print('position:')
    print(position)
    print('div_term:')
    print(div_term)


# https://towardsdatascience.com/unit-testing-in-deep-learning-b91d366e4862
def test_positional_encoding():
    input_sentence = "Good Morning! What are your plans today?"
    input_indices = [char_to_index(c) for c in input_sentence]

    assert input_indices == ([71, 111, 111, 100, 32, 77, 111, 114,
                          110, 105, 110, 103, 33, 32, 87, 104, 
                          97, 116, 32, 97, 114, 101, 32, 121, 
                          111, 117, 114, 32, 112, 108, 97, 110, 
                          115, 32, 116, 111, 100, 97, 121, 63])
    
    


if __name__ == '__main__':
    test_positional_encoding()
