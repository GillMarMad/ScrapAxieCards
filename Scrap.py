import requests
from bs4 import BeautifulSoup

webpage = requests.get('https://www.axieworld.com/en/tools/cards-explorer')

soup = BeautifulSoup(webpage.text, 'html.parser')

# class_ =  soup.find( class_ = "_1yvIbAXHlIpl5Dhrx8xBB-" ).extract()
# subclass = class_.select('div._15NnuVhmyNHKrZ0lLQ6AA_ _1pKms34Og1H5tn4CbKu6NQ')
# # print(webpage.text)
# print(subclass)





#####




# a='''<div class="quoteText">
#       “Don't cry because it's over, smile because it happened.”
#   <br/>  -
#     <a class="authorOrTitle" href="/author/show/61105.Dr_Seuss">Dr. Seuss</a>
# </div>, <div class="quoteText">'''
# s=BeautifulSoup(a,'lxml')
# s.find(class_="authorOrTitle").extract()
# print(s.text)



# a='''<div>
# <li class="test">
#     <a>link1</a>
#     <ul> 
#        <li>  
#           <a>link2</a> 
#        </li>
#     </ul>
# </li>
# </div>'''

# soup = BeautifulSoup(a, 'html.parser')
# li = soup.find('li', {'class': 'test'})
# children = li.findChildren("a" , recursive=True)
# for child in children:
#     print(child)


# print(soup.select('div._15NnuVhmyNHKrZ0lLQ6AA_ _1pKms34Og1H5tn4CbKu6NQ'))

# for i in soup.select('div._15NnuVhmyNHKrZ0lLQ6AA_ _1pKms34Og1H5tn4CbKu6NQ'):
#     print(i.string)

a = 'https://storage.googleapis.com/axie-cdn/game/cards/base/beast-mouth-02.png'
toremove = 'https://storage.googleapis.com/axie-cdn/game/cards/base/'
# b = a.replace(toremove, '').replace('.png','')
# c = result = ''.join(i for i in b if not i.isdigit())
guion_cout = 0
result = ''
for i in a.replace(toremove, ''):
    if(guion_cout == 1):
        result += i
    if(i == '-'):
        guion_cout += 1
result = result.replace('-', '')
print(result)
