# Extracting Data from JSON

import urllib.request as ur
import json

url = input("Enter location: ")
print('Retrieving', url)

total = 0
count = 0

data = ur.urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
obj = json.loads(data)

for item in obj["comments"]:
    count = count + 1
    total = total + int(item['count'])

print('Count: ', count)
print('Sum: ', total)