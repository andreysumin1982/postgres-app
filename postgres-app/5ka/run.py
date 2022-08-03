#from bs4 import BeautifulSoup as bs
from parser import Parser
#
def run():
    HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    # try:
    #     response = Parser(url, HEADERS)
    #     result = response.getHTML()
    #     with open(save_file, 'w') as file:
    #         file.write(result.text)
    # except Exception:
    #     return


    response = Parser(url, HEADERS)
    result = response.getHTMLSelenium()
    print(type(result))
    with open(save_file, 'w') as file:
        file.write(result)


if __name__ == '__main__':
    print(Parser.__doc__)
    url = 'https://edadeal.ru/sankt-peterburg/retailers/5ka'
    #url = 'https://wttr.in/%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3'
    save_file = '/home/asumin/web-app/postgres-app/5ka/dataset.html'
    #run()

