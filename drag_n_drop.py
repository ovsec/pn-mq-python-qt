
from pathlib import Path
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt
from PySide6.QtCore import QObject, QUrl, Property, Signal

from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QComboBox, QHBoxLayout, QListWidget, QListWidgetItem
from PySide6.QtQuick import QQuickView
import sys


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
                           background-color: #111;
                           color: white;
                           """)
        self.setWindowTitle("Drag and Drop")
        self.resize(720, 480)
        
        
        l1 = QLabel()
        l1.setText("Hello World")

        self.cb = QComboBox()
        self.cb.setStyleSheet("""
                           width: 100%;
                            min-width: 15ch;
                            max-width: 30ch;
                            border: 1px solid #111;
                            border-radius: 0.25em;
                            padding: 0.25em 0.5em;
                            font-size: 1.25rem;
                            line-height: 1.1;
                            background-color: #222;
                            background-image: linear-gradient(to top, #191919, #111 33%);
                           """)
        
        self.cb.addItems(["OIO_TEST", "OIO_PROD", "SCANNED_SWE"])
        self.cb.currentIndexChanged.connect(self.selectionchange)
        
        self.d = DragnDropWidget(self)
        # d.show()
        vbox = QVBoxLayout()
        self.s = SideMenuWidget(2)
        vbox.addWidget(self.cb, 1)
        # vbox.addWidget(l1)
        vbox.addWidget(self.d, 4)
        
        self.setLayout(vbox)
        

    

    def selectionchange(self,i):
      print("Items in the list are :")
      self.d.l1.setText(f'Selected queue {self.cb.currentText()}')
      for count in range(self.cb.count()):
         print (self.cb.itemText(count))
      print ("Current index",i,"selection changed ",self.cb.currentText())



class SideMenuWidget(QtWidgets.QWidget):
    def __init__(self, selectedIndex):
        super().__init__()
        self.setStyleSheet("""
                           color: white;
                           """)
        
        
        vbox = QVBoxLayout()
        self.menu_widget = QListWidget()
        for i in range(10):
            item = QListWidgetItem(f"Item {i}")
            item.setTextAlignment(Qt.AlignCenter)
            
            self.menu_widget.addItem(item)
            if i == selectedIndex:
                self.menu_widget.setCurrentItem(item)
        
        vbox.addWidget(self.menu_widget)
        self.setLayout(vbox)



class DragnDropWidget(QtWidgets.QWidget):
    def __init__(self, Parent):
        super().__init__()
        self.setAcceptDrops(True)
        self.l1 = QLabel()
        self.l1.setText("Hello World")
        self.l1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        l = QVBoxLayout()
        l.addWidget(self.l1)
        self.setLayout(l)
        self.setStyleSheet("""
                           border-radius: 0.25em;
                           padding: 0.25em 0.5em;
                           font-size: 3rem;
                           background-color: #222;
                           width: 100%;
                           height: 100%; 
                           color: white;
                           border: 1px dashed #888;
                           border-radius: 20px;
                           """)

    def dragEnterEvent(self, event):
        self.setStyleSheet("""
                           background-color: #444;
                           border: 1px dashed white
                           """)
        self.l1.setText("Drop the file...")
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            print(f)
    
    def dragLeaveEvent(self, event):
        self.setStyleSheet("""
                           background-color: #222;
                           width: 100%;
                           height: 100%; 
                           color: white;
                           border: 1px dashed #888;
                           border-radius: 20px;
                           """)
        self.l1.setText("Drag and drop files here.")
        
        

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ui = MainWidget()
    
    ui.show()

    """ with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style) """
    sys.exit(app.exec())