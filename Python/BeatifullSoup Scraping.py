#imports of python modules
import requests
from bs4 import BeautifulSoup
#Setting the url we will be requesting from
url = 'http://books.toscrape.com/'

#using headers because a lot of sites require it
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

#requesting the source with python requests and parsing it to lxml for beatifullsoup to use
source = requests.get(url, headers=headers)
soup = BeautifulSoup(source.text,"lxml")
#gets site title
title = soup.title.text
#scrapes all product + info
for Books in soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3'):
    name = Books.find('h3').a.get('title')
    href = Books.find('h3').a.get('href')
    #The href is only part of the link here we making it a full link
    url = 'http://books.toscrape.com/'+href
    picture = Books.find('img').get('src')
    PictureLink = 'http://books.toscrape.com/'+picture
    #An other way to do it. Searching on attributes
    price = Books.find(attrs={'class':'price_color'}).text.strip('Â')

    #While scraping the prices load with having a 'Â' in front of it. We used .strip() to remove that specif character
    #You can also leave the strip function empty and it will remove all the spaces from the text.

