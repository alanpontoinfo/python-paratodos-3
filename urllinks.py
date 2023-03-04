import urllib.request, urllib.parse,urllib.error 
from bs4 import BeautifulSoup

url = input('Enter -')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# recupera todos de links tag 

tags= soup('a')
for tag in tags:
    print(tag.get('href', None))