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
    #print(s.getCounters('ezreal'))
    #s.runes('ezreal')
    #s.populateRunes()
    s.getRunes("ezreal")

class Scraper:
    def __init__(self):
        self.counter_dict = {}
        self.runes_dict = {}
        self.champions = []
        self.home_url = "https://u.gg/lol/champions"
        self.options = Options()
        self.options.headless = True

        self.driver = webdriver.Firefox(options=self.options)

    def initialize(self):
        self.driver.get(self.home_url)
        results = self.driver.find_elements_by_xpath("//*[@class='champions-container']")

        self.champions = results[0].text.split('\n')


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

    def runes(self, champ):
        runes = []
        champ = champ.replace(" ", "").replace("'", "").replace(".", "")
        url = self.home_url + f'/{champ.lower()}/build'

        self.driver.get(url)

        keystone_obj = self.driver.find_elements_by_xpath("//*[@class='perk keystone perk-active']")

        keystone = self.cleanRunes(keystone_obj[0], "Keystone ")
        runes.append(keystone)

        runes_obj = self.driver.find_elements_by_xpath("//*[@class='perk perk-active']")

        i = 0
        while i < 5:
            rune = self.cleanRunes(runes_obj[i], "Rune ")
            runes.append(rune)
            i+=1

        shards_obj = self.driver.find_elements_by_xpath("//*[@class='shard shard-active']")

        j = 0
        while j < 3:
            shard = self.cleanRunes(shards_obj[j], 'alt="')
            runes.append(shard)
            j+=1

        return runes


    def populateCounters(self):
        self.initialize()

        print("stage 1 complete")
        count = 0

        for champ in self.champions:
            try:
                counters = self.counters(champ)
                self.counter_dict[champ] = counters
            except Exception as e:
                print("Counter Error")
                self.counter_dict[champ] = "No data for this champ"
                continue # CHANGE TO BREAK IF NOT WORKING
            count+=1
            print("{}%".format(math.floor((count/len(self.champions)*100))))
        print("Counters populated")



        self.driver.quit()
        counterfile = open('counterfile', 'w')
        json1 = json.dumps(dict1)
        counterfile.write(json1)
        counterfile.close()

    def populateRunes(self):
        self.initialize()
        count = 0

        for champ in self.champions:
            try:
                runes = self.runes(champ)
                self.runes_dict[champ] = runes
            except Exception as e:
                print("Rune Error")
                self.runes_dict[champ] = "No data for this champ"
                continue
            count+=1
            print("{}%".format(math.floor((count/len(self.champions)*100))))


        self.driver.quit()
        runefile = open('runefile', 'w')
        json1 = json.dumps(dict1)
        runefile.write(json1)
        runefile.close()


    def getCounters(self, champ):
        champ = champ.lower()
        champ = champ.capitalize()
        infile = open('counterfile', 'r')
        x = infile.read()

        full_dict = json.loads(x)

        return full_dict[champ]

    def getRunes(self, champ):
        champ = champ.lower()
        champ = champ.capitalize()
        infile = open('runefile', 'r')
        x = infile.read()

        full_dict = json.loads(x)

        return full_dict[champ]

    def test(self):
        dict1 = {}

        counterfile = open('counterfile', 'w')
        json1 = json.dumps(dict1)
        counterfile.write(json1)
        counterfile.close()

    def cleanRunes(self, html_object, split):
        rune = html_object.get_attribute("innerHTML")
        rune = rune.split(split, 1)[1]
        rune = rune[0:-2]

        return rune


main()
