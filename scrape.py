import requests
from bs4 import BeautifulSoup
import re
from numpy import random

from model import gpt_eng_to_deu

base_url = "https://en.wikipedia.org/wiki/"

MIN_SENTENCE_LENGTH = 100
N_RETURNS = 5

def clean(text):
    clean_text = re.sub('<.*?>', '', text) # remove tags
    clean_text = clean_text.replace('\n', '')
    clean_text = re.sub(r'\s+', ' ', clean_text) # replaces multiple spaces with a single one
    #clean_text = re.sub(r'\[\d+\]', '', clean_text) # remove citations
    clean_text = re.sub(r'\[.+?\]', '', clean_text) # remove citations
    clean_text = re.sub(r'\s+([.,:;!?])', r'\1', clean_text) # remove spaces before punctuation

    return clean_text

def scrape_wiki(item):
    # item: search item
    # will then scrape from base_url + item
    # to see how to use this function,
    # run test2() in test_scrape.py

    response = requests.get(base_url + item)
    soup = BeautifulSoup(response.content, "html.parser")
    # https://stackoverflow.com/questions/58402962/beautifulsoup4-find-function-not-working
    soup = BeautifulSoup(soup.prettify(), "html.parser")
    try:
        paragraphs = soup.find_all('p')
        
    except:
        print('scraping does not work')

    cnt = 0
    for p in paragraphs:
        if cnt >= N_RETURNS:
            break

        p_clean = clean(p.get_text())
        if len(p_clean) >= MIN_SENTENCE_LENGTH:
            yield p_clean
            cnt += 1


def generate_data():
    # from the paragraphs returned by scrape_wiki,
    # I want to pick a random word w and then
    # call scrape_wiki(w) to generate another
    # set of paragraphs

    for p in scrape_wiki('Norway'):
        de = gpt_eng_to_deu(p)


'''
def f():
    which_paragraph = random.choice(N_RETURNS)
    cnt = 0
    for p in scrape_wiki('Norway'):
        if cnt == which_paragraph:
            

        cnt += 1
'''

'''
def select_next_word():
    # randomly selects the next word to search in wiki
'''
    


