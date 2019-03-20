"""
This program is designed to crawl latest Donald Trump news from cnn.com and twitter
and show the results in a website
Author: Luwei Wang
Update Date:03/20/2019
"""


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.chrome.options import Options
from flask import Flask,render_template

#selenium + headless Chrome
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#executable_path should be your Chromedriver.exe installation path
driver_cnn = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\Chromedriver.exe",chrome_options=options)
driver_twi = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\Chromedriver.exe",chrome_options=options)
wait = ui.WebDriverWait(driver_twi, 10)
wait = ui.WebDriverWait(driver_cnn,10)

#DonaldTrump Twitter url
base_url_t = u'https://twitter.com/'
query_t = u'realDonaldTrump'
url_t = base_url_t+query_t

#CNN news search results url
url_c = "https://edition.cnn.com/search/?q=Donald%20Trump&size=25&page=1"

driver_cnn.get(url_c)
driver_twi.get(url_t)
#time.sleep(1)

#crawl data from twitter, put each tweet (text,multimedia urls) into list_t
body_t = driver_twi.find_element_by_tag_name('body')
tweets = driver_twi.find_elements_by_class_name('content')
list_t=[]

for tweet in tweets[0:30]:
    tweettext = tweet.find_elements_by_class_name('tweet-text')
    if tweettext:

        if len(tweettext) == 2:
            twi = tweettext[0].text + '\n' + tweettext[1].text
        else:
            twi = tweettext[0].text
        try:
            tweet.find_element_by_class_name('AdaptiveMediaOuterContainer')
            a = True
        except:
            a = False

        if a == True:
            statusid=tweet.find_element_by_class_name('AdaptiveMediaOuterContainer').find_element_by_xpath('..').find_element_by_xpath('..').get_attribute('data-permalink-path')
            video_url = base_url_t + statusid
        else:
            video_url = 0
        list_t.append((twi,video_url))

#crawl data from cnn.com, put article (title, url) into list_c
list_c=[]
for headline in driver_cnn.find_elements_by_class_name('cnn-search__result-headline'):
    list_c.append((headline.text,headline.find_element_by_xpath("a").get_attribute('href')))

#use Flask to render html
app = Flask(__name__)

@app.route('/')
def index(list_twi = None, list_cnn = None):
    return render_template('index.html',list_twi = list_t,list_cnn = list_c)

if __name__ == '__main__':
    app.run(debug=True)
