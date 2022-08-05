import requests
from selenium import webdriver
from selenium_stealth import stealth
import time
from error.error import saveFileError
#
class Stealth:
    ''''''
    def __init__(self, url, headers = None):
        self.url = url
        self.headers = headers or None

    def getHTMLStealth(self):
        try:
            # Делаем GET-запрос
            response = requests.get(url=self.url, headers=self.headers, timeout=5)
            if response.status_code != 200: # код ответа сервера
                print(f"[OK] {self.url} {response.status_code}\n")
            #
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")

            # headless mode (браузер в фоновом режиме)
            #options.add_argument("--headless")

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

            # Делаем GET-запрос и ждем 15 сек
            driver.get(self.url)
            print(f"[OK] => GET-запрос {self.url}")
            time.sleep(15)
        except Exception as EX:
            # Пишем ошибки в лог.
            saveFileError(self.url, EX)
        else:
            # Возвращаем результат
            print(f" [+] => Получили HTTP-контент")
            return driver.page_source
        finally:
            # Закрываем соединение и браузер
            driver.close();
            driver.quit()
#
if __name__ == '__main__':
    pass