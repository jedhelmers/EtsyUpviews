class etsyListing():
    def __init__(self, shop, link):
        self.shop = shop
        self.link = link

# clear && printf '\e[3J'

import urllib2
from bs4 import BeautifulSoup
import requests

url = requests.get('https://www.etsy.com/search?q=planner+stickers+clear')
listTest = []

data = url.text

soup = BeautifulSoup(data, 'lxml')

#print soup
#soup = BeautifulSoup(urllib2.urlopen(url).read(), "lxml")

#bodyCopies = soup.find_all(class_ = 'listing-link')
cnt = 0
for foo in soup.find_all('div', attrs={'class': 'v2-listing-card'}):
    try:
        shoplink = foo.find('a', attrs={'class': 'listing-link'})
        shop = foo.find('p', attrs={'class': 'mr-xs-1'})
        listTest.append(etsyListing(shop.text, shoplink['href']))
        #print shop.text, shoplink['href']#, cnt
    except:
        print ''
    cnt += 1

for shop in listTest:
    if shop.shop.upper() == 'PENANDNIBS':
        
        print shop.shop
        print "%s \n" % shop.link
