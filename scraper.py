from bs4 import BeautifulSoup
import requests
import time
import math
import json
from selenium import webdriver

from selenium.webdriver.firefox.options import Options

def main():
    s = Scraper()
    #s.initialize()
    #s.populate()
    #s.test()
    print(s.getCounters('ezreal'))

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
            champ = champ.replace(" ", "").replace("'", "").replace(".", "")
            url = self.home_url + f'/{champ.lower()}/counter'
        print(url)

        champ_counters = []
        tmp = []
        self.driver.get(url)
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

        #time.sleep(5)

        results = self.driver.find_elements_by_xpath("//*[@class='counters-list best-win-rate']")
        #print(results[0].text)
        if results == None:
            return
        indexes = results[0].text.split('\n')
        for i in range(0, len(indexes)-2, 3):
            tmp = [indexes[i], indexes[i+1], indexes[i+2]]
            champ_counters.append(tmp)
        return champ_counters


    def populateCounters(self):
        self.initialize()

        print("stage 1 complete")
        count = 0

        for champ in self.champions:
            try:
                counters = self.counters(champ)
                self.counter_dict[champ] = counters
            except Exception as e:
                print("Error")
                self.counter_dict[champ] = "No data for this champ"
                continue # CHANGE TO BREAK IF NOT WORKING
            count+=1
            print("{}%".format(math.floor((count/len(self.champions)*100))))



        self.driver.quit()
        dictfile = open('dictfile', 'w')
        json1 = json.dumps(dict1)
        dictfile.write(json1)
        dictfile.close()

    def populateRunes(self):


    def getCounters(self, champ):
        champ = champ.lower()
        champ = champ.capitalize()
        infile = open('dictfile', 'r')
        x = infile.read()

        full_dict = json.loads(x)

        return full_dict[champ]

    def test(self):
        dict1 = {}

        dictfile = open('dictfile', 'w')
        json1 = json.dumps(dict1)
        dictfile.write(json1)
        dictfile.close()


main()
