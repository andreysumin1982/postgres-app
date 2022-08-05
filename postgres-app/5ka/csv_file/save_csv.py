#
import csv
from datetime import datetime
#
csv_file = '/home/asumin/web-app/postgres-app/5ka/'
#
def save(data=None):
    file_name = datetime.now().strftime('%m-%d-%Y')
    with open(f"{csv_file}{file_name}.csv", "w") as file:
        writer = csv.writer(file, delimiter=";")  # Отделяем стобцы (;)
        writer.writerow(["Продукт", "Кол-во", "Акция", "Цена по акции", "Старая цена", "Изображение", "Дата"]) # Шапка
        for key, value in data.items():
            try:
                writer.writerow([key,
                    value[0],
                    value[1],
                    value[2],
                    value[3],
                    value[4],
                    datetime.now().replace(microsecond=0)
                ])
            except Exception:
                print(f"[SAVE ERROR] => {key} {value}")
                continue
    #
    print(f"[OK] => {csv_file}{file_name}.csv")
#
if __name__ == '__main__':
    pass
    #save()