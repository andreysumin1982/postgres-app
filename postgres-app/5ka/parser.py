import requests
from selenium import webdriver
from selenium_stealth import stealth
import time
from datetime import datetime
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
            time.sleep(2)
            if retry:   # Повторная попытка соединения. До 3 раз
                print(f"[INFO] retry = {retry} => {self.url}")
                return self.getHTML(retry - 1)  # Вызываем метод, уменьшая попытку на 1
            else:
                # Пишем ошибки в лог.
                error_log = '/home/asumin/web-app/postgres-app/5ka/error.log'
                dt = datetime.now().replace(microsecond=0)      # Убираем микросекунды
                error = f"{dt}\n[ERROR] => {self.url}\n{EX}\n\n"
                with open(error_log, 'a') as file:
                    file.write(error)
                print(f"[ERROR] => {error_log}\n")
        else:
            return response
    #
    def getHTMLSelenium(self):
        ''''''
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")

            # options.add_argument("--headless")

            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            driver = webdriver.Chrome(options=options,
                                      executable_path="/usr/bin/chromedriver",
                                      )


            stealth(driver,
                    languages=["en-US", "en"],
                    vendor="Google Inc.",
                    platform="Win32",
                    webgl_vendor="Intel Inc.",
                    renderer="Intel Iris OpenGL Engine",
                    fix_hairline=True,
                    )



            # Делаем GET-запрос и ждем 5 сек
            driver.get(self.url)
            time.sleep(15)
        except Exception as EX:
            print(f"[ERROR] => {EX}\n")
        else:
            return driver.page_source
        finally:
            driver.close(); driver.quit()

#
if __name__ == '__main__':
    pass