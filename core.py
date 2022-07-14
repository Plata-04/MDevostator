from ast import keyword
import requests
from bs4 import BeautifulSoup
import re
import csv
post_id = ""
title = ""
keywords = ""
URL = "https://gp-19.ru/savina-galina-stepanovna-stati/vyvih-rastyazhenie-i-perenapryazhenie-kapsulno-svyazochnogo-apparata-plechevogo-poyasa/"
data = []

data = [
            ['ID', 'Type', 'Keywords (ILJ)', 'Title', 'Url'],
            ['21319', 'post', 'ляля,ляля', 'London', 'https://expluataciya-holodilnika.ru/voprosy-i-otvety-po-ekspluatatsii-holodilnika/kak-perevezti-holodilnik-bez-upakovki-pri-pereezde/'],
                ]



def pars():
    global post_id, title, URL
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'lxml')
    title = re.sub(r'[^\w\s]','', soup.select('h1.entry-title')[0].text.strip()).lower()
    post_id = re.sub('[^0-9]', '', soup.find("article").get("id"))
    print(title, post_id)
    
def black_lister():
    global keywords, title
    title = set(title.split())
    b_list = {"как", "термопакетом"}
    keywords = ",".join(list(title.difference(b_list)))

def csv_data():
    global post_id, title, keywords, URL, data
    data_head = ['ID', 'Type', 'Keywords (ILJ)', 'Title', 'Url']
    data_pre = [post_id, "post", keywords, title, URL]
    if not data:
        data.append(data_head)
    data.append(data_pre)



def csv_writer():
    global data
    with open('test.csv', 'w', newline='', encoding="utf_8") as csvfile:
        writer = csv.writer(csvfile, quotechar='"', delimiter = ";", dialect='unix')
        for row in data:
            writer.writerow(row)

