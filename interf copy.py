
from msilib.schema import Directory
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtCore import QTimer, QEventLoop
from PyQt5.QtWidgets import QMessageBox
import os
import requests
from bs4 import BeautifulSoup
import re
import csv
import time
import sys
from threading import *

prog_bar = 0
kof = 0
URLS = []
sleep = 0
post_id = ""
title = ""
keywords = ""
black_list = []
URL = ""
data = []
#https://gp-19.ru/savina-galina-stepanovna-stati/vyvih-rastyazhenie-i-perenapryazhenie-kapsulno-svyazochnogo-apparata-plechevogo-poyasa/


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(resource_path('untitled.ui'), self)
        self.show()
        self.load()
        self.start.clicked.connect(self.Start)
        self.open_.clicked.connect(self.open)

    def Start(self):
        if self.textURL.toPlainText():
            global URLS, black_list, sleep, kof, prog_bar, data

            URLS = self.textURL.toPlainText().split("\n")
            URLS = list(filter(None, URLS))

            data = []
            prog_bar = 0
            kof = 100/len(URLS)

            black_list = self.textblack.toPlainText().split("\n")
            black_list = list(filter(None, black_list))

            self.start.setDisabled(True)
            self.textURL.setDisabled(True)
            self.textblack.setDisabled(True)
            self.spinBox.setDisabled(True)

            sleep = self.spinBox.value()

            self.save()
            self.pars()
            self.csv_writer()
            
            self.progressBar.setValue(100)

            self.textURL.setDisabled(False)
            self.textblack.setDisabled(False)
            self.spinBox.setDisabled(False)   
            self.start.setDisabled(False)

     
    def open(self):
        directory = "result"

        if not os.path.isdir("result"):
            os.mkdir("result")
        os.system(f'start {directory}')

    def load(self):
        if os.path.isfile("blacklist.txt"):
            global black_list
            with open("blacklist.txt", "r") as file:
                for word in file:
                    word = word.replace("\n", "")
                    self.textblack.append(word)
                    black_list.append(word)

    def save (self):
        global black_list
        with open("blacklist.txt", "w") as file:
            for word in black_list:
                file.write(str(word) + "\n")
        

    def str_time(self): #название файла м-д-ч-м-с
        named_tuple = time.localtime() # получить struct_time
        time_string = time.strftime("%m-%d-%H-%M-%S", named_tuple)
        return time_string  

    def pars(self):
        global post_id, title, URL, URLS, sleep, kof, prog_bar
        for url in URLS:
            try:
                URL = url
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'lxml')
                title = re.sub(r'[^\w\s]','', soup.select('h1.entry-title')[0].text.strip()).lower()
                post_id = re.sub('[^0-9]', '', soup.find("article").get("id"))
                self.black_lister()
                self.csv_data()
                prog_bar = prog_bar + kof
                self.progressBar.setValue(int(prog_bar))
                if sleep:
                    loop = QEventLoop()
                    QTimer.singleShot(sleep, loop.quit)
                    loop.exec_()
            except: 
                prog_bar = prog_bar + kof
                continue
            

            

        
    def black_lister(self):
        global keywords, title, black_list
        title1 = set(title.split())
        b_list = set(black_list)
        keywords = ",".join(list(title1.difference(b_list)))

    def csv_data(self):
        global post_id, title, keywords, URL, data
        data_head = ['ID', 'Type', 'Keywords (ILJ)', 'Title', 'Url']
        data_pre = [post_id, "post", keywords, title, URL]
        if not data:
            data.append(data_head)
        data.append(data_pre)


    def csv_writer(self):
        global data
        if not os.path.isdir("result"):
            os.mkdir("result")
        name = str(self.str_time())
        with open(f"result\\{name}.csv", 'w', newline='', encoding="utf_8") as csvfile:
            writer = csv.writer(csvfile, quotechar='"', delimiter = ";", dialect='unix')
            for row in data:
                writer.writerow(row)








app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()