
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox
import os
import requests
from bs4 import BeautifulSoup
import re
import csv
import time
import sys
from threading import *

post_id = ""
title = ""
keywords = ""
URL = "https://gp-19.ru/savina-galina-stepanovna-stati/vyvih-rastyazhenie-i-perenapryazhenie-kapsulno-svyazochnogo-apparata-plechevogo-poyasa/"
data = []

data = [
            ['ID', 'Type', 'Keywords (ILJ)', 'Title', 'Url'],
            ['21319', 'post', 'ляля,ляля', 'London', 'https://expluataciya-holodilnika.ru/voprosy-i-otvety-po-ekspluatatsii-holodilnika/kak-perevezti-holodilnik-bez-upakovki-pri-pereezde/'],
                ]


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



# class Ui(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(Ui, self).__init__()
#         uic.loadUi(resource_path('untitled.ui'), self)
#         self.show()

#     def str_time(self): #название файла м-д-ч-м-с
#         named_tuple = time.localtime() # получить struct_time
#         time_string = time.strftime("%m-%d-%H-%M- %S", named_tuple)
#         return time_string

#     def pars(self):
#         global post_id, title, URL
#         response = requests.get(URL)
#         soup = BeautifulSoup(response.text, 'lxml')
#         title = re.sub(r'[^\w\s]','', soup.select('h1.entry-title')[0].text.strip()).lower()
#         post_id = re.sub('[^0-9]', '', soup.find("article").get("id"))
#         print(title, post_id)
        
#     def black_lister(self):
#         global keywords, title
#         title = set(title.split())
#         b_list = {"как", "термопакетом"}
#         keywords = ",".join(list(title.difference(b_list)))

#     def csv_data(self):
#         global post_id, title, keywords, URL, data
#         data_head = ['ID', 'Type', 'Keywords (ILJ)', 'Title', 'Url']
#         data_pre = [post_id, "post", keywords, title, URL]
#         if not data:
#             data.append(data_head)
#         data.append(data_pre)


#     def csv_writer(self):
#         global data
#         with open('test.csv', 'w', newline='', encoding="utf_8") as csvfile:
#             writer = csv.writer(csvfile, quotechar='"', delimiter = ";", dialect='unix')
#             for row in data:
#                 writer.writerow(row)








# app = QtWidgets.QApplication(sys.argv)
# window = Ui()
# app.exec_()