from bs4 import BeautifulSoup
import requests
import time
import math
from selenium import webdriver

from selenium.webdriver.firefox.options import Options

def main():
    s = Scraper()
    #s.initialize()
    s.createCountersDict()

class Scraper:
    def __init__(self):
        self.counter_dict = {}
        self.champions = []
        self.home_url = "https://u.gg/lol/champions"
        self.options = Options()
        self.options.headless = True

        self.driver = webdriver.Firefox(options=self.options)

    def initialize(self):
        self.driver.get(self.home_url)
        results = self.driver.find_elements_by_xpath("//*[@class='champions-container']")
        #print(results[0].text.split('\n'))
        self.champions = results[0].text.split('\n')
        #return self.champions

        #self.driver.quit()

    def counters(self, champ):
        if champ == "Nunu & Willump":
            url = self.home_url + "/nunu/counter"
        else:
            url = self.home_url + f'/{champ.lower().replace(" ", "")}/counter'
        print(url)

        #champ_counters = []
        self.driver.get(url)
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

        #time.sleep(5)

        results = self.driver.find_elements_by_xpath("//*[@class='counters-list best-win-rate']")
        #print(results[0].text)
        if results == None:
            return
        champ_counters = list(results[0].text)
        return champ_counters


    def createCountersDict(self):
        self.initialize()
        print(len(self.champions))
        print("stage 1 complete")
        count = 0

        for champ in self.champions:
            counters = self.counters(champ)
            self.counter_dict[champ] = counters

            count+=1
            print("{}%".format(math.floor(count/len(self.champions))))
            time.sleep(1)


        self.driver.quit()
        print(self.counter_dict)

main()
