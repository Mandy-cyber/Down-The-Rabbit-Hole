from get_chrome_driver import GetChromeDriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import time
import random

# subthemes = ['feminist literature', 
#             'queer love letters', 
#             'top horror novels turned to movies',
#             'top 10 fanfictions',
#             'most tear-jerking poems']
subtheme = 'top 10 fanfiction'

def set_up_page(subtheme):
    # get_driver = GetChromeDriver() 
    # get_driver.install()
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--log-level=3")
    # options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)
    browser.get("https://www.wikipedia.com")
    searchbar = browser.find_element_by_name("search")
    searchbar.send_keys(subtheme)
    searchbar.send_keys(Keys.RETURN)
    url = browser.current_url
    word = "search="
    if word in url:
        newUrls = find_pages(url)
    else:
        page = requests.get(url)
        ramen = BeautifulSoup(page.content, 'html.parser')
        paras = ramen.find_all("p", class_="")[0:5]
        paragraphs = []
        for para in paras:
            print(para.text)
            paragraphs.append(para.text)
        # return paragraphs
    return url


def find_pages(url):
    page = requests.get(url)
    ramen = BeautifulSoup(page.content, 'html.parser')
    names = ramen.find_all("li", class_="mw-search-result") #, class_="mw-search-result-heading"
    newUrls = []
    for name in names[:2]:
        name = name.find("a")['href']
        new_url = f"https://www.wikipedia.com/{name}"
        newUrls.append(new_url)
    return newUrls

def find_multiple_info(newUrls):
    paragraphs = []
    for url in newUrls:
        page = requests.get(url)
        ramen = BeautifulSoup(page.content, 'html.parser')
        paras = ramen.find_all("p", class_="")[0:5]
        for para in paras:
            print(para.text)
            paragraphs.append(para.text)
    return paragraphs

url = set_up_page(subtheme)
newUrls = find_pages(url)



# def find_info(url):
#     page = requests.get(url)
#     ramen = BeautifulSoup(page.content, 'html.parser')
#     paras = ramen.find_all("p", class_="")[0:5]
#     paragraphs = []
#     for para in paras:
#         print(para.text)
#         paragraphs.append(para.text)
#     return paragraphs
        


# print(newUrls)




'''
THE PLAN
---------------------
- function takes user input as variable
- input = a word, phrase or really anything that can be searched
- function randomly selects site from preapproved list to scrape
- get first two paragraphs or maybe 200 words?
- run it through a loop so every x amount of words, it inserts a new line
- randomly choose a word from the new paragraph 
- return both the new word and the 2 paragraphs

'''