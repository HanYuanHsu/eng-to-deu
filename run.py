from model import *
from utils import *
from scrape import *

sentence1 = "We use both first and third-party cookies to personalise web content, analyse visits to our websites and tailor advertisements. Some of these cookies are necessary for the website to function, whilst others require your consent. More detail can be found in our cookie policy and you can tailor your choices in the preference centre."

def run1():
    print(gpt_eng_to_deu(sentence1))

def run2():
    print(gpt_eng_to_deu("What does 'homomorphism' even mean?"))

def run3():
    print(gpt_eng_to_deu("bird"))

def test_utils():
    for p in scrape_wiki('Norway'):
        print(p)
        print('------------')
        indices = [char_to_index(c) for c in p]
        print(indices)
        print('------------')
        pp = ''.join([index_to_char(i) for i in indices])
        print(pp)

def run4():
    """
    Arguments:
        x: Tensor, shape ``[seq_len, batch_size, embedding_dim]``
    """
    return 0


def run5():
    pos = PositionalEncoding(d_model=100)


run4()
