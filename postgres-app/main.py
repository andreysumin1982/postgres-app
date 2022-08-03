# Импортируем модуль connectdb
from connectdb import Postgres
# Импортируем модуль readfile
from readfile import File
#
import json
#
def fillTable():
    # Заполняем таблицы
    l = Postgres('localhost', 'language_db', 'test', 'test')
    file = File(pathfile)
    # Бежим по файлу
    for key, value in file.read().items():
        # заполняем таблицу language
        l.executeRequest(f"insert into language (name) values ('{key}');")
        # Узнаем последний (максимальный) id
        id = l.executeRequest(f"select max(id) from language;")
        # Конвертируем данные в словарь
        id_str = ''.join(l.convertResult(id).get(0))
        # Заполняем таблицу release
        l.executeRequest(f"insert into release (id_lang, year) values ({int(id_str)},'{int(value)}');")
#
def filltablejson():
    #
    cars_db = Postgres('localhost', 'cars_db', 'test', 'test')
    file = File(pathjson)
    result = file.readJson()
    #
    for key ,value in result['list'].items():
        print('*', key)
        # заполняем таблицу brand
        cars_db.executeRequest(f"insert into brand (name) values ('{key}');")
        # Узнаем последний (максимальный) id
        id = cars_db.executeRequest(f"select max(id) from brand;")
        # Конвертируем данные в словарь
        id_str = ''.join(cars_db.convertResult(id).get(0))
        for item in value:
            #print(' -',item)
            # Заполняем таблицу model
            cars_db.executeRequest(f"insert into model (id_brand, name) values ({int(id_str)},'{item}');")
#

#
def run():
    # Экземпляр класса
    #db_lang = Postgres('localhost', 'language_db', 'test', 'test')
    #
    #result1 = db_lang.executeRequest('select * from language')
    #result2 = db_lang.executeRequest('select * from release')
    #result3 = db_lang.executeRequest('select language.id, language.name, release.year from language '
    #                                 'join release on release.id_lang = language.id;')


    cars_db = Postgres('localhost', 'cars_db', 'test', 'test')
    res = cars_db.executeRequest('select brand.name, model.name from brand '
                                     'join model on model.id_brand = brand.id;')
    #
    res_convert = cars_db.convertResult(res)
    d = {}
    for key, value in res_convert.items():
        if value[0].strip() not in d:
            d[value[0].strip()] = []
            d[value[0].strip()].append(value[1])
        else:
            d[value[0].strip()].append(value[1])
    print(d)
    #cars_db.deleteRows('brand')

#

if __name__ == '__main__':
    pathfile = '/home/asumin/web-app/postgres-app/language'
    pathjson = '/home/asumin/web-app/postgres-app/json/carsBase-master/cars.json'
    run()
    # for i in range(1):
    #     filltablejson()