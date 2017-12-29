import random

def rndIP(max):
    rndIpList = []
    for i in range (1,max+1):
        ip = format(random.randint(1,255))+"."+format(random.randint(1,255))+"."+format(random.randint(1,255))+"."+format(random.randint(1,255))
        rndIpList.append(ip)
    #print rndIpList
    return rndIpList
