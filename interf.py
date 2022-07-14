
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox
import os
import sys
from threading import *
import socket
import cv2



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












app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()