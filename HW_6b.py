# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')
position = int(input('Enter position: '))
count = int(input('Enter count: '))
url_lst = []
tag_lst = []

for num in range(count):
	print ('Retrieving', url)
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	tag_lst = []
	for tag in tags:
		tag_lst.append(tag)
	url = tag_lst[position-1].get('href', None)
	url_lst.append(url)
print (url_lst[-1])

