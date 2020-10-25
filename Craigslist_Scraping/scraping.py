from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt

def scrape_all(city, item):

    #initilize the browser
    browser = Browser('chrome',executable_path="/usr/local/bin/chromedriver", headless=True)

    data = {
        "Item Title": get_title(browser,city, item)
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
    
    try:

        title = mysoup.select("ul.rows li.result-row h2 a")

        for text in title:

            item_titles = {}

            my_title = text.get_text()

            item_titles['item_title']=my_title

            item_titles_collection.append(item_titles)
    except: 
        print("Your script failed to scrape.")
    
    return item_titles_collection
    