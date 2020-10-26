from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt

def scrape_all(city, item):

    #initilize the browser
    browser = Browser('chrome',executable_path="/usr/local/bin/chromedriver", headless=True)

    data = {
        "craigs_listing_title": get_title(browser,city, item)
    }

    browser.quit()
    return data

def get_title(browser, city, item): 
    browser = Browser("chrome",executable_path="/usr/local/bin/chromedriver", headless=True)

    url = f"https://{city}.craigslist.org/search/sss?sort=rel&query={item}"
    html = browser.visit(url)

    html = browser.html

    item_titles_collection=[]

    mysoup = soup(html, "html.parser")

    all_titles = mysoup.select("ul.rows li.result-row")[0:12]

    for text in all_titles:

        title = {}

        try:

            my_title = text.select_one('h2 a').get_text()

            title['item_title']=my_title

            link = text.select_one('h2 a')['href']

            browser.visit(link)

            html= browser.html

            mysoup = soup(html,'html.parser')

            img_url = mysoup.select_one('div.swipe img')['src']

            title['image']=img_url

            price = text.select_one('span.result-price').get_text()

            title['price']=price

            item_titles_collection.append(title)


        
        except:
            print('something went wrong with the scraping')
    
    
    return item_titles_collection
    