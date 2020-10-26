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

    all_titles = mysoup.select("ul.rows li.result-row h2 a")[0:12]

    for text in all_titles:

        title = {}

        try:

            my_title = text.get_text()

            title['item_title']=my_title
            
            link = text['href']
            
            browser.visit(link)
            
            html= browser.html
            
            mysoup = soup(html,'html.parser')
            
            img_url = mysoup.select_one('div.swipe img')['src']
            
            title['image']=img_url

            item_titles_collection.append(title)
        
        except:
            print('something went wrong with the scraping')
    
    
    return item_titles_collection
    