from datetime import datetime
#
def saveFileError(url, error):
    # Пишем ошибки в лог.
    error_log = '/home/asumin/web-app/postgres-app/5ka/error/error.log'
    dt = datetime.now().replace(microsecond=0)  # Убираем микросекунды
    text_error = f"{dt}\n[ERROR] => {url}\n{error}\n\n"
    with open(error_log, 'a') as file:
        file.write(text_error)
    print(f" [ERROR] => {error_log}\n")
#
if __name__ == '__main__':
    pass