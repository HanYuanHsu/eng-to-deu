from scrape import *

content1 = '''
Association football is the most popular sport in Norway in terms of active membership. In 2014–2015 polling, football ranked far behind
           <a href="/wiki/Biathlon" title="Biathlon">
            biathlon
           </a>
           and
           <a href="/wiki/Cross-country_skiing_(sport)" title="Cross-country skiing (sport)">
            cross-country skiing
           </a>
           in terms of popularity as spectator sports.
           <sup class="reference" id="cite_ref-Spopop_307-0">
<a href="#cite_note-Spopop-307">
             [301]
            </a>
'''
def test1():
    return clean(content1)

def test2():
    for p in scrape_wiki('food'):
        print(p)
        print('----------')

test2()
