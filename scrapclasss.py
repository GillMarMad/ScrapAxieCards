from  bs4 import BeautifulSoup
import requests, time

class CrawledArticle():

    def __init__(self, heading, message):
        self.heading = heading
        self.message = message

class ArticleFetcher():

    def fetch(self):
        url = "https://www.axieworld.com/en/tools/cards-explorer"
        articles = []
        time.sleep(1)
        r = requests.get(url)  
        doc1 = BeautifulSoup(r.text, "lxml")
        doc = doc1.find(class_='_1yvIbAXHlIpl5Dhrx8xBB-')

        for item in doc.select('div._15NnuVhmyNHKrZ0lLQ6AA_ _1pKms34Og1H5tn4CbKu6NQ'):
            print("hi")
            heading = item.select_one('._1xgANzDmpUnFoGof4hpR1f').text.strip()
            # message = item.select_one('.msg-content-cell .p-msg-head-body:not(.pull-right)').text.strip()
            crawled = CrawledArticle(heading, "")
            articles.append(crawled)

        return articles

a = ArticleFetcher()
b = a.fetch()
for item in b:
    print(item.heading,'\n' ,item.message)