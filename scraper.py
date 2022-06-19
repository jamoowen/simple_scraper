import requests
from bs4 import BeautifulSoup
import pprint

# hackernews now uses .titlelink instead of storylink class

res  = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titlelink')
subt = soup.select('.subtext')


def sort_stories(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def create_hn(links, subt):
    hn =[]
    for i, item in enumerate(links):
        title = links[i].getText()
        href = links[i].get('href', None)
        v = subt[i].select('.score')
        if len(v):
            points = int(v[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes':points})

    return sort_stories(hn)

pprint.pprint(create_hn(links, subt))