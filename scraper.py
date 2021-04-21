from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options


def counters(champ):
    url = f"https://u.gg/lol/champions/{champ}/counters"
    page = requests.get(url)
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options)
    driver.get(url) #? page ?
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

    #time.sleep(5)

    results = driver.find_elements_by_xpath("//*[@class='counters-list best-win-rate']")
    return results[0].text
    driver.quit()

    #soup = BeautifulSoup(page.content, 'html.parser')





#def counters():
