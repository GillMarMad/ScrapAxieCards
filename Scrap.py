import requests
from bs4 import BeautifulSoup
import urllib.request
import csv

class AxieCard():
    def __init__(self, name, axietype, energycost, bodyname, type, attack, shield, effect, url):
        self.name = name
        self.axietype = axietype
        self.energycost = energycost
        self.bodyname = bodyname
        self.type = type
        self.attack = attack
        self.shield = shield
        self.effect = effect
        self.url = url
        self.bodypart = self.getboypart()
        # self.downloadImage()

    def getboypart(self):
        toremove = 'https://storage.googleapis.com/axie-cdn/game/cards/base/'
        substring = self.url.replace(toremove, '')
        guion_cout = 0
        result = ''
        for i in substring:
            if(guion_cout == 1):
                result += i
            if(i == '-'):
                guion_cout += 1
        result = result.replace('-', '')
        return(result)
    def downloadImage(self):
        path = f"data\{self.axietype}\{self.name}.png"
        urllib.request.urlretrieve(self.url, path)

Cards = []
webpage = requests.get('https://www.axieworld.com/en/tools/cards-explorer')
soup = BeautifulSoup(webpage.text, 'html.parser')

container = soup.find('div', {'class': '_1yvIbAXHlIpl5Dhrx8xBB-'})

fishes = container.find_all('div', {'class': '_15NnuVhmyNHKrZ0lLQ6AA_ _1pKms34Og1H5tn4CbKu6NQ'})
beasts = container.find_all('div', {'class': '_15NnuVhmyNHKrZ0lLQ6AA_ _2d_vRHP3mVO8wmejm-tGlh'})
birds = container.find_all('div', {'class': '_15NnuVhmyNHKrZ0lLQ6AA_ _2zxwFgu0tfI9LuVrbdQ_BA'})
bugs = container.find_all('div', {'class': '_15NnuVhmyNHKrZ0lLQ6AA_ _3sWQhiYI4gx2cSAeiYSGHL'})
plants = container.find_all('div', {'class': '_15NnuVhmyNHKrZ0lLQ6AA_ _1cXFCtO9_xVPtC5p8Ix8HQ'})
reptiles = container.find_all('div', {'class': '_15NnuVhmyNHKrZ0lLQ6AA_ _1E0n_excNTxC35T2zuA8t9'})

axieTypes = {'Fish' : fishes, 'Beast' : beasts, 'Bird' : birds, 'Bug' : bugs, 'Plant' : plants, 'Reptil' : reptiles}

for key, values in axieTypes.items():
    for item in values:
        elements = []
        elements.append(key)
        fish_bodypartname = item.find('div', {'class': '_1xgANzDmpUnFoGof4hpR1f'}).text
        fish_atack_type = item.find('div', {'class': '_2Fy55eQWQ3NBHXr2Uno_fd'}).text
        elements.append(fish_bodypartname)
        elements.append(fish_atack_type)
        fish_elements = item.find_all('div', {'class': '_2rANcuS_Le2SELI6Fjht7B'})
        for i in fish_elements:
            spans = i.find_all('span')
            for span in spans:       
                elements.append(span.text)
            url = (i.find('img')['src'])
            elements.append(url)
        # for element in elements:
        #     print(element)
        # print("\n ------------ ")
        card = AxieCard(elements[3], elements[0], elements[4], elements[1], elements[2], elements[5], elements[6], elements[7], elements[8])
        # card.downloadImage()
        Cards.append(card)


#Create CSV File
header = ['name','bodyname','bodypart','energycost','type','attack','shield','effect','axietype','Imageurl']
data = []
for card in Cards:
    data.append([card.name, card.bodyname, card.bodypart, card.energycost, card.type, card.attack, card.shield, card.effect, card.axietype, card.url])
with open('AxieCards.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)