from bs4 import BeautifulSoup
from modules.parser import Parser
from modules.stealth import Stealth
from time import sleep
#
def getStealthHTML(url, step=None, retry=None):
    try:
        st = Stealth(url)
        result = st.getHTMLStealth()
        #print(type(result))
        with open(save_file, 'a') as file:
            file.write(result)
        print(f" [+] => save {save_file}")
    except: return
#
def getPages():
    count = 3  # int(''.join(lastpage))
    for item in range(1, count+1):
        page = f'https://edadeal.ru/sankt-peterburg/retailers/5ka?page={item}'
        sleep(2)
        getStealthHTML(page, item, count)
        print(f" [+] => {item}/{count}\n")
#
def processData(data_file):
    with open(data_file) as file:
        result = file.read()
    #
    soup = BeautifulSoup(result, 'html.parser')
    #
    #pages = soup.findAll('div', class_='b-button__content')
    #lastpage = [item.get_text() for item in pages[-2:-1]]
    #count = 30  # int(''.join(lastpage))
    #links = []  # Список всех страниц
    cards = soup.find_all('div', class_='b-offer__root')  # Получаем карточки товаров
    #
    error_list = []
    dataset={}
    for card in cards:  # Вытаскиваем названия продукта
        try:
            product_name = card.find('div', class_='b-offer__product-info').find('div', class_='b-offer__description')
            quanity = card.find('div', class_='b-offer__product-info').find('div', class_='b-offer__quantity')
            data_discount = card.find('div', class_='b-offer__offer-info').find('div', class_='b-offer__dates')
            price_new = card.find('div', class_='b-offer__footer').find('div', class_='b-offer__price-new')
            price_old = card.find('div', class_='b-offer__footer').find('div', class_='b-offer__price-old')
            image = card.find('div', class_='b-offer__header').find('img', class_='b-image__img')
            # print(f"{product_name.get_text()}\n"
            #       f"{quanity.get_text()}\n"
            #       f"{data_discount.get_text()}\n"
            #       f"{price_new.get_text()}\n"
            #       f"{price_old.get_text()}\n"
            #       f"{image['src']}\n")

            if product_name.get_text() not in dataset:
                dataset[product_name.get_text()] = []
            dataset[product_name.get_text()].append(quanity.get_text())
            dataset[product_name.get_text()].append(data_discount.get_text())
            dataset[product_name.get_text()].append(price_new.get_text())
            dataset[product_name.get_text()].append(price_old.get_text())
            dataset[product_name.get_text()].append(image['src'])

        except:
            error_list.append(f"[INFO] => {product_name}\n")
            continue
    print(dataset)

    #
    for k,v in dataset.items():
        print(k,''.join(v))

#
if __name__ == '__main__':
    #print(Parser.__doc__)
    #url = 'https://edadeal.ru/sankt-peterburg/retailers/5ka'
    #url = 'https://wttr.ini/%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3'
    save_file = '/home/asumin/web-app/postgres-app/5ka/dataset3.html'
    #getPages()
    processData(save_file)

