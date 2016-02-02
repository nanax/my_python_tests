# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

def p(li):
    url = li
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    tag = tags[17]
    print tag.get('href', None)
    return tag.get('href', None)
n=7
a="http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Iona.html"
while True:
    if n==0:
        break
    else:
        n=n-1
        a=p(a)
ai=raw_input("djsck")