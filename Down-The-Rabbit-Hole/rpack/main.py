from get_chrome_driver import GetChromeDriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random

# subthemes = ['feminist literature', 
#             'queer love letters', 
#             'top horror novels turned to movies',
#             'top 10 fanfictions',
#             'most tear-jerking poems']
subtheme = 'top 10 fanfictions'

def set_up():
    get_driver = GetChromeDriver() 
    get_driver.install()
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--log-level=3")
    browser = webdriver.Chrome(options=options)
    return browser

def scrape_wiki(subtheme, browser):
    browser.get("https://www.wikipedia.com")
    searchbar = browser.find_element_by_name("search")
    searchbar.send_keys(subtheme)
    searchbar.send_keys(Keys.RETURN)

# def scrape_citi(subtheme):
#     print("")

# def scrape_brit(subtheme):
#     print("")



# def make_selection(subtheme):
#     websites = ['britannica', 'citizendium', 'wikipedia']
#     website = random.choice(websites)
#     if website == 'britannica':
#         scrape_brit(subtheme)
#     elif website == 'citizendium':
#         scrape_citi(subtheme)
#     else:
#         scrape_wiki(subtheme)
#     return



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