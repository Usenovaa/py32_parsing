
import requests
from bs4 import BeautifulSoup
import csv


def write_to_csv(data: dict):
    with open('data.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow((data['title'], data['price'], data['img'], data['desc']))


def get_html(url):
    response = requests.get(url)
    # print(response.status_code) 
    # print(response.text)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    cars = soup.find('div', class_='catalog-list').find_all('a')
    # print(cars)
    for car in cars:
        try:
            title = car.find('span', class_='catalog-item-caption').text.strip()
        except:
            title = ''

        try:
            price = car.find('span', class_='catalog-item-price').text
        except:
            price = ''

        try:
            desc = car.find('span', class_="catalog-item-descr").text.split()
            desc = ' '.join(desc)
        except:
            desc = ''

        try:
            img = car.find('img').get('src')
        except:
            img = ''


        data = {
            'title': title,
            'price': price,
            'desc': desc,
            'img': img
        }

        write_to_csv(data)
        
        # print(img)
        # print(car)
        # print('===========================')



def main():
    url = 'https://cars.kg/offers'
    html = get_html(url)
    get_data(html)



with open('data.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(['title          ', 'price       ', 'image          ', 'description         '])


main()