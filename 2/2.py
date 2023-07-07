import os
from pathlib import Path
import sys
import random
from os.path import dirname, join
from turtle import width

from PyQt5.Qt import *     
from PyQt5.QtGui import QPainter, QColor                                       # PyQt5
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSignal



class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.load_ui()
        
    def paintEvent(self, event):
        if self.do_paint:
            polos= QPainter()
            polos.begin(self)
            self.draw_flag(polos)
            polos.end()
 
    def paint(self):
        self.do_paint = True
        self.repaint()

    
    def draw_flag(self, polos):
        x_2 = 50
        for i in range(1,self.numb+1):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            polos.setBrush(QColor(r, g, b))
            polos.drawRect(30, (x_2*i), 350, 50)
        
    def spawn_flag(self,numb):
        self.numb = numb
        self.paint()

    def load_ui(self):
        #os.chdir('F:\Project\Py\Widget_art')
        current_dir = dirname(__file__)
        file_path = join(current_dir, "./1_wind.ui")
        uic.loadUi(file_path , self)
        self.add_numb.clicked.connect(self.onClicked)
        

    
    def onClicked(self):
        self.w2 = Window2()
        
        self.w2.show()  
        self.w2.numb_of_rock[int].connect(self.spawn_flag)
        self.do_paint = False




class Window2(QWidget):
    numb_of_rock = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.load_ui()
        
    def load_ui(self):
        #os.chdir('F:\Project\Py\Widget_art')
        current_dir = dirname(__file__)
        file_path = join(current_dir, "./2_wind.ui")
        uic.loadUi(file_path , self)
        self.btn_ok.clicked.connect(self.onClicked)
        self.btn_no.clicked.connect(self.onClicked_no)

    def onClicked_no(self):
        self.close()

    def onClicked(self):
        self.numb_of_rock.emit(int(self.numb.text()))
        self.close()
        

if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())


