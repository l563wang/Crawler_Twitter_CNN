# Crawler_Twitter_CNN
a crawler that crawls the 25 latest articles from cnn.com about Donald Trump and his 20 latest tweets and a website that shows the results 

Language:
python,
html

IDE:
PyCharm

Dependencies:
Selenium,
Flask,
chromedriver

Usage:
1.Download the zip, unzip it, in the path where CNNTwiCrawler.py is located, create a document named"templates", move "index.html" to the "templates" document. Then python CNNTwiCrawler.py
2.enter "http://127.0.0.1:5000/" in the browser address bar,then you can see the results of news and tweets.

Website Introduce:
1.You can click one of the article titles to look at the detailed information.
2.I planed to crawl 25 tweets but twitter seems to have a safeguard to allow users to crawl no more than 20 tweets, I have not found a method to bypass it until now.
3.If a tweet contains a video or a picture,there is a button named "media", you can click it to have a look at the detailed information.
