import requests
from bs4 import BeautifulSoup
import re

base_url = "https://en.wikipedia.org/wiki/"

def clean(text):
    clean_text = re.sub('<.*?>', '', text) # remove tags
    clean_text = clean_text.replace('\n', '')
    clean_text = re.sub(r'\s+', ' ', clean_text) # replaces multiple spaces with a single one
    clean_text = re.sub(r'\[\d+\]', '', clean_text) # citations

    return clean_text

def scrape_wiki(item):
    # item: search item
    # will then scrape from base_url + item
    # returns a 

    response = requests.get(base_url + item)
    soup = BeautifulSoup(response.content, "html.parser")
    # https://stackoverflow.com/questions/58402962/beautifulsoup4-find-function-not-working
    soup = BeautifulSoup(soup.prettify(), "html.parser")
    try:
        paragraphs = soup.find_all('p')
        
    except:
        print('scraping does not work')
    
    return [clean(p.get_text()) for p in paragraphs]



if __name__ == '__main__':
    ps = scrape_wiki('Norway')
    for p in ps:
        print(p)
        print('-------------')
        print('-------------')


