import os
from sys import argv
from urllib.parse import urlparse

user_news_sites = '/home/user/.news_sites'

url=argv[1]
npdir = newspaper.__file__[:-11] + 'resources/misc/'
gs = open(npdir+'google_sources.txt','r')
ps = open(npdir+'popular_sources.txt','r')
us = open(user_news_sites,'r')
news_sites = []
for s in [gs,ps,us]:
    news_sites.extend(s.read().split('\n'))
    s.close()
site = urlparse(url).netloc

def run(args): os.spawnvp(os.P_NOWAIT, 'uh', args)

def news(url):
    a=newspaper.Article(url)
    a.download()
    a.parse()
    o=open('.newsarticle','w')
    if a.summary:
        o.write(a.summary+'\n\n')
    for l in a.text.split('\n'):
        o.write(l+'\n')
    o.write('-----\n')
    if a.authors:
        o.write(','.join(a.authors)+'\n')
    if a.publish_date:
        dateStr = a.publish_date.strftime("%d-%b-%Y %H:%M:%S")
        o.write(dateStr+'\n')
    o.write(url)
    o.close
    run(['uh.sh','news','.newsarticle'])
    
def youtube(url):
    print(url)
    run(['uh.sh','yt',url])

if site in news_sites:
    news(url)
elif site in ['m.youtube.com','www.youtube.com','youtu.be']:
    youtube(url)
else:
    run(['uh.sh','web',url])
