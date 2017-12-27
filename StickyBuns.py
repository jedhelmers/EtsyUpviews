import subprocess
import sys
from anonBrowser import *
from randomIP_List import *
import time
import random

random.seed(4453)

rand1 = random.uniform(1,3)


max = 60
tempIP = []
tempIP = rndIP(max)
#print len(tempIP)

urlList = []
urlList = ["https://www.etsy.com/search?q=pen+and+nibs+stickers", "https://www.etsy.com/shop/PenandNibs?ref=search_shop_redirect", "https://www.etsy.com/listing/571579765/this-weeks-menu-monday-sunday-clear?ref=shop_home_active_1", "https://www.etsy.com/listing/556050426/monthly-habit-tracker-hand-lettered?ref=shop_home_active_2", "https://www.etsy.com/listing/556047244/hourly-time-strip-hand-lettered-clear?ref=shop_home_active_3", "https://www.etsy.com/listing/568251713/months-of-the-year-hand-lettered-clear?ref=shop_home_active_4", "https://www.etsy.com/listing/551990140/2018-mini-calendars-hand-lettered-clear?ref=shop_home_active_5", "https://www.etsy.com/listing/565786049/holidays-2-hand-lettered-clear-matte?ref=shop_home_active_6", "https://www.etsy.com/listing/549558316/2018-calendars-hand-lettered-clear-matte?ref=shop_home_active_7", "https://www.etsy.com/listing/560221643/chores-hand-lettered-clear-matte-planner?ref=shop_home_active_8", "https://www.etsy.com/listing/560220569/shopping-hand-lettered-clear-matte?ref=shop_home_active_9", "https://www.etsy.com/listing/560219513/relax-hand-lettered-clear-matte-planner?ref=shop_home_active_10", "https://www.etsy.com/listing/560215353/celebrate-hand-lettered-clear-matte?ref=shop_home_active_11", "https://www.etsy.com/listing/560214207/holidays-hand-lettered-clear-matte?ref=shop_home_active_12", "https://www.etsy.com/listing/555948451/oops-misfit-grab-bag-planner-stickers?ref=shop_home_active_13", "https://www.etsy.com/listing/552384191/bullet-point-to-do-list-clear-matte?ref=shop_home_active_14", "https://www.etsy.com/listing/538580666/hello-my-name-is-half-box-labels-clear?ref=shop_home_active_15", "https://www.etsy.com/listing/537065512/work-hand-lettered-clear-matte-planner?ref=shop_home_active_16", "https://www.etsy.com/listing/537064588/cleaning-hand-lettered-clear-matte?ref=shop_home_active_17", "https://www.etsy.com/listing/550863073/days-of-the-week-hand-lettered-clear?ref=shop_home_active_18", "https://www.etsy.com/listing/550862131/date-night-hand-lettered-clear-matte?ref=shop_home_active_19", "https://www.etsy.com/listing/550860967/goals-hand-lettered-clear-matte-planner?ref=shop_home_active_20", "https://www.etsy.com/listing/550859879/date-numbers-hand-lettered-clear-matte?ref=shop_home_active_21", "https://www.etsy.com/listing/550858897/weekend-hand-lettered-clear-matte?ref=shop_home_active_22", "https://www.etsy.com/listing/550857271/birthday-hand-lettered-clear-matte?ref=shop_home_active_23", "https://www.etsy.com/listing/550855637/this-week-hand-lettered-clear-matte?ref=shop_home_active_24", "https://www.etsy.com/listing/550854971/laundry-hand-lettered-clear-matte?ref=shop_home_active_25", "https://www.etsy.com/listing/537054092/rent-hand-lettered-clear-matte-planner?ref=shop_home_active_26", "https://www.etsy.com/listing/537051704/groceries-hand-lettered-clear-matte?ref=shop_home_active_27", "https://www.etsy.com/listing/550824289/to-buy-hand-lettered-clear-matte-planner?ref=shop_home_active_28", "https://www.etsy.com/listing/537019700/this-month-hand-lettered-clear-matte?ref=shop_home_active_29", "https://www.etsy.com/listing/537018546/days-of-the-week-hand-lettered-clear?ref=shop_home_active_30", "https://www.etsy.com/listing/537017490/bills-hand-lettered-clear-matte-planner?ref=shop_home_active_31", "https://www.etsy.com/listing/537011064/months-of-the-year-hand-lettered-clear?ref=shop_home_active_32"]

ab = anonBrowser(proxies=tempIP, user_agents=[('User-agent','superSecretBrowser')])
#for attempt in range(1,5
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
    sys.exit()