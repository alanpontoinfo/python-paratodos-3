import urllib.request, urllib.parse,urllib.error 
from bs4 import BeautifulSoup
import ssl

#ignore erros do certificado ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Entre -' )
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# recupera todas tags links
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))