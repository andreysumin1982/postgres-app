#
import json
#
class File:
    def __str__(self):
        return "* Класс для работы с файлом *"
    #
    def __init__(self, path):
        self.path = path
    #
    def readfile(self):
        """Метод читает файл возвращает словарь"""
        with open(self.path) as file:
            result = {' '.join(item.split()[:-1]):item.split()[-1] for item in file.readlines()}
        return result
    #
    def readJson(self):
        with open(self.path) as file:
            result = json.load(file)
        return result
#
if __name__ == '__main__':
    pass
