#Import Libs
import requests as req
from bs4 import BeautifulSoup
from list_offers import list_offers
from deep_translator import GoogleTranslator
from urllib.parse import urlunparse, urlparse
#Connect to trendyol
trendyol_ = req.get('https://www.trendyol.com/')

#Load HTML
print('[-] Connecting to https://www.trendyol.com/ ...')
soup = BeautifulSoup(trendyol_.text, 'html.parser')
print('[+] Connected.')

#Extract Data 
categories = soup.find_all('li', {'class': 'tab-link'})
cat_dict = {}

#Maintain Links and Translate data
print('[-] Translating Data... Please Wait (Categories list)')
for cat in categories:
    url_parts = list(urlparse(cat.a['href']))
    url_parts[0] = 'https'
    url_parts[1] = 'www.trendyol.com'
    url = urlunparse(url_parts)
    name_translated = GoogleTranslator(source='tr', target='en').translate(cat.a.contents[0])
    cat_dict[name_translated] = url
print('[+] Translation Task Finished. \n')
print('--------------------------------------------------------')
#Get Category name
for each in cat_dict:
    print(each)

cat_in = input('Enter an category name to view its daily offers > ')
try:
    category = cat_dict[cat_in.upper()]
except KeyError:
    print('Category does not exist.')
    exit()
list_offers(category)
