from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options

def main():
    s = Scraper()
    #print(s.initialize())

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

        self.champions = results[0].text.split()
        #return self.champions

        #self.driver.quit()

    def counters(self, champ):
        url = self.home_url + f'{champ}/counters'

        champ_counters = []
        self.driver.get(url)
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

        #time.sleep(5)

        results = self.driver.find_elements_by_xpath("//*[@class='counters-list best-win-rate']")
        champ_counters.append(results[0].text)
        return champ_counters


    def createCountersDict(self):
        self.initialize()
        print("stage 1 complete")
        count = 0

        for champ in self.champions:
            counters = self.counters(champ)
            self.counter_dict[champ] = counters

            count+=1
            print("{}%".format(count//len(self.champions)))
            time.sleep(1)


        self.driver.quit()
        print(self.counter_dict)

main()
