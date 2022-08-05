import requests
from time import sleep
from error.error import saveFileError
#
class Parser:
    '''
    Класс для парсинга HTML-страниц:
        1. Создать объект (экземпляр класса Parser): obj = Parser(url)
        2. Метод getHTML, для полечения WEB-контента: obj.getHTML()
        3. Метод getHTMLSelenium, для полечения WEB-контента SPA: obj.getHTMLSelenium()
    '''
    def __init__(self, url, headers = None):
        self.url = url
        self.headers = headers or None
    #
    def getHTML(self, retry=3):
        ''' Метод создает GET-запрос и возвращает полученный WEB-контент'''
        try:
            # Делаем GET-запрос
            response = requests.get(url=self.url, headers=self.headers, timeout=5)
            # код ответа сервера
            print(f"[OK] {self.url} {response.status_code}\n")
        except Exception as EX:
            sleep(2)
            if retry:   # Повторная попытка соединения. До 3 раз
                print(f"[INFO] retry = {retry} => {self.url}")
                return self.getHTML(retry - 1)  # Вызываем метод, уменьшая попытку на 1
            else:
                # Пишем ошибки в лог.
                saveFileError(self.url, EX)
        else:
            return response

#
if __name__ == '__main__':
    pass