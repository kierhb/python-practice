# Following Links in Python

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
position = int(input('Enter position: ')) - 1
count = int(input('Enter count: '))
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')
Sequence = []
href = soup('a')

for i in range(count):
    link = href[position].get('href', None)
    print('Retrieving: ', link)
    Sequence.append(href[position].contents[0])
    html = urllib.request.urlopen(link, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    href = soup('a')
    link = href[position].get('href', None)

print(Sequence[-1])