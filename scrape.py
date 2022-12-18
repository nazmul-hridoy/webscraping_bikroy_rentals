from bs4 import BeautifulSoup
import requests
from csv import writer




url = "https://bikroy.com/en/ads/bangladesh/apartment-rentals"
page = requests.get(url)
# print(page)  #ok
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)  #ok
lists = soup.find_all('div', class_="container--2uFyv")
#print(lists)
with open('bikroy_tolet.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Description', 'Rent']
    thewriter.writerow(header)
    for values in lists:
        title = values.find('h2', class_="heading--2eONR").text.replace('\n',  '')
        description = values.find('div', class_="description--2-ez3").text.replace('\n',  '')
        rent = values.find('div', class_="price--3SnqI color--t0tGX").text.replace('\n', '')
        info = [title, description, rent]
        thewriter.writerow(info)
