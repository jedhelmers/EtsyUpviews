import subprocess
import sys
from anonBrowser import *
from randomIP_List import *
import time
import random
import datetime

f = open('searchTracker.txt', 'a+')

class etsyListing():
    def __init__(self, shop, link):
        self.shop = shop
        self.link = link



# clear && printf '\e[3J'

import urllib2
from bs4 import BeautifulSoup
import requests

searchList = ['https://www.etsy.com/search?q=planner+stickers+clear',
    'https://www.etsy.com/search?q=planner+stickers+pen',
    'https://www.etsy.com/search?q=clear+planner+stickers',
    'https://www.etsy.com/search?q=days+of+the+week+stickers&as_prefix=days+of+the+week+&explicit=1&page=2',
    'https://www.etsy.com/search?q=planner+stickers+clear&page=2',
    'https://www.etsy.com/search?q=planner+stickers+pen&page=2',
    'https://www.etsy.com/search?q=clear+planner+stickers&page=2',
    'https://www.etsy.com/search?q=planner+stickers+clear&page=3',
    'https://www.etsy.com/search?q=planner+stickers+pen&page=3',
    'https://www.etsy.com/search?q=clear+planner+stickers&page=3',
    'https://www.etsy.com/search?q=planner%20stickers',
    'https://www.etsy.com/search?q=planner+stickers&explicit=1&page=2',
    'https://www.etsy.com/search?q=planner+stickers&explicit=1&page=3',
    'https://www.etsy.com/search?q=planner+stickers&explicit=1&page=4']

listTest = []
urlList = []


for searchListItem in searchList:
    url = requests.get(searchListItem)
    data = url.text
    soup = BeautifulSoup(data, 'lxml')

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

    now = datetime.datetime.now()
    for shop in listTest:
        xcnt = 0
        #print shop.shop, shop.link
        if shop.shop.upper() == 'PENANDNIBS':
            urlList.append((shop.link).replace(' ', '%20'))
            #print shop.link
            xcnt += 1
    f.write("Results Count: \n%s\nDate: %s \nQuery\n%s\n\n" % (xcnt, now.strftime('%Y-%m-%d'), searchListItem))
            #print shop.shop
            #print "%s \n" % shop.link

random.seed(4453)
f.close()

rand1 = random.uniform(1,3)
#print urlList

max = 60
tempIP = []
tempIP = rndIP(max)

#print urlList

ab = anonBrowser(proxies=tempIP, user_agents=[('User-agent','superSecretBrowser')])
#print len(ab.proxies)
try:
    for attempt in ab.proxies:
        print '[*] ' + format(attempt)
        ab.anonymize()
        print '[*] Fetching page'
        for urlItem in urlList:
            #print urlItem
            try:
                response = ab.open(urlItem)
            except:
                response = ""
            for cookie in ab.cookie_jar:
                print cookie
            time.sleep(rand1)
        #for prox in ab.proxies:
        #    print prox
        for usr in ab.user_agents:
            print '[-] User Agent ' + format(usr)
        print '\n\n'

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    f.close()
    sys.exit()
