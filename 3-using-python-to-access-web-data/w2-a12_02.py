#Scraping Numbers from HTML using BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
xsum = 0

tags = soup('span')
for tag in tags:
    lines = ('Contents: ', tag.contents[0])
    num = list(lines)
    y = int(num[1])
    if y > 0:
        xsum = xsum + y

print(xsum)