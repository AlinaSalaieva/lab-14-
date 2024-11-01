import os
import requests
import json

class Holiday:
    def __init__(self, date, name):
        self.date = date
        self.name = name

    def __str__(self):
        return f"{self.date} - {self.name}"

country = input("Введіть країну (us, ua): ")

content = requests.get("https://date.nager.at/api/v3/publicholidays/2024/" + country).content
holidaysJson = json.loads(content)

holidayList = [Holiday(holiday['date'], holiday['name']) for holiday in holidaysJson]

output_directory = "12341"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

with open(os.path.join(output_directory, "holidays.txt"), "w", encoding='utf-8') as file:
    finalString = "\n".join(str(h) for h in holidayList)
    file.write(finalString)

print("Файл зі святами успішно збережено.")