from model import *

sentence1 = "We use both first and third-party cookies to personalise web content, analyse visits to our websites and tailor advertisements. Some of these cookies are necessary for the website to function, whilst others require your consent. More detail can be found in our cookie policy and you can tailor your choices in the preference centre."

def run1():
    print(gpt_eng_to_deu(sentence1))

def run2():
    print(gpt_eng_to_deu("What does 'homomorphism' even mean?"))

def run3():
    print(gpt_eng_to_deu("bird"))

run2()
