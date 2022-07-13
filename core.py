# import requests
# from bs4 import BeautifulSoup
# import re

# URL = "https://gp-19.ru/savina-galina-stepanovna-stati/vyvih-rastyazhenie-i-perenapryazhenie-kapsulno-svyazochnogo-apparata-plechevogo-poyasa/"

# response = requests.get(URL)
# soup = BeautifulSoup(response.text, 'lxml')
# title = re.sub(r'[^\w\s]','', soup.select('h1.entry-title')[0].text.strip()).lower()
# post_id = re.sub('[^0-9]', '', soup.find("article").get("id"))
# #title = set(title.split())
# # b_list = {"как", "термопакетом"}
# # title = title.difference(b_list)
# print(title, post_id)

from codecs import utf_16_be_decode
import csv

import csv

with open('test.csv', 'w', encoding="utf_16") as csvfile:
    fieldnames = ['"ID"', '"Type"', '"Keywords (ILJ)"', '"Title"', '"Url"']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,quotechar="|", delimiter = ";")

    writer.writeheader()
    writer.writerow({'"ID"': '"21319"', '"Type"': '"post', '"Keywords (ILJ)"': '"перевезти,упаковки,переезде,перевозить,упаковка,переезд"', '"Title"': '"Как перевезти холодильник без упаковки при переезде?"', '"Url"': '"https://expluataciya-holodilnika.ru/voprosy-i-otvety-po-ekspluatatsii-holodilnika/kak-perevezti-holodilnik-bez-upakovki-pri-pereezde/"'})


