#Import Libs
from bs4 import BeautifulSoup
import re
import requests as req
import sys
from time import sleep
from urllib.parse import urlparse, urlunparse
from deep_translator import GoogleTranslator

def list_offers(category_link):
    #Connect to trendyol
    try:
        trendyol = req.get(category_link)
    except:
        trendyol = req.get(category_link)

    print('[-] Finding Offers')
    #Load HTML
    soup = BeautifulSoup(trendyol.text, 'html.parser')

    #Extract Data
    offers_div = soup.find('div', {'class' : 'sticky-wrapper'})
    offers_list = offers_div.find_all('article')
    print('[+] Offers Found.')
    offers = {}
    print('[-] Translating Data... Please Wait (Offers list)')
    #Maintain links and translate data
    for link in offers_list:
        url_parts = list(urlparse(link.a['href']))
        url_parts[0] = 'https'
        url_parts[1] = 'www.trendyol.com'
        url = urlunparse(url_parts)
        name_translated = GoogleTranslator(source='tr', target='en').translate(link.a.summary.span.contents[0])
        offers[name_translated] = url
    print('[+] Translation Task Finished. \n\n')

    #Print Scrapped data
    for offer in offers:
        print('------------------------------------')
        print('Name: ', offer)
        print('Link: ', offers[offer])
