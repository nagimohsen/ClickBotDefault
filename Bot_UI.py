from PyQt5.QtCore import pyqtSlot, QThread, Qt
from PyQt5.QtGui import QIcon, QGuiApplication
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout,
                             QGroupBox, QHBoxLayout, QComboBox, QLineEdit, QMessageBox, QLabel, QProgressBar, QTextEdit,
                             QCheckBox, QSizePolicy)
import sys


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()



    def initUI(self):

        self.title = 'Insta Bot Post Adoptable Pet Info'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 300



        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        

        self.label=QLabel(self)
        self.label.move(20,20)
        self.label.setText('Phone/mail')
        
        

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(100, 20)
        self.textbox.resize(200,25)

        ##################################


        self.Pasword_lbl=QLabel(self)
        self.Pasword_lbl.move(20,50)
        self.Pasword_lbl.setText('Password')

        
        

        # Create textbox
        self.Pasword_txt = QLineEdit(self)
        self.Pasword_txt.move(100, 50)
        self.Pasword_txt.resize(200,25)
        self.Pasword_txt.setEchoMode(QLineEdit.Password)

        # Create filter_label

        self.filter_lbl=QLabel(self)
        self.filter_lbl.move(350,30)
        self.filter_lbl.setText('No Of Posts To Make')


        # Create filter_cat_list
        self.filter_cat_list=QComboBox(self)
        self.filter_cat_list.addItem('1')
        self.filter_cat_list.addItem('2')
        self.filter_cat_list.addItem('3')
        self.filter_cat_list.addItem('4')
        self.filter_cat_list.addItem('5')
        self.filter_cat_list.addItem('6')
        self.filter_cat_list.addItem('7')
        self.filter_cat_list.addItem('8')
        self.filter_cat_list.addItem('9')
        self.filter_cat_list.move(460,28)
        




        #create a label


        self.Note_lbl=QLabel(self)
        self.Note_lbl.move(200,170)
        
        self.Note_lbl.setText('Note : script may not work properly when there is slow internet connection')
        self.Note_lbl.resize(500,20)
        #self.Note_lbl.style("bold")
        
        
        # Create a button in the window
        self.button = QPushButton('Start Bot', self)
        self.button.move(330,140)
        
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()




    @pyqtSlot()
    def on_click(self):

        Instagram_id = self.textbox.text().strip()
        Instagram_password=self.Pasword_txt.text()
        No_Of_Posts_To_Make_str=self.filter_cat_list.currentText()
        

        if str(Instagram_id)=="":
            QMessageBox.question(self, 'Message - pythonspot.com', "User name empty", QMessageBox.Ok, QMessageBox.Ok)
            return

        if str(Instagram_password)=="":
            QMessageBox.question(self, 'Message - pythonspot.com', "Password empty", QMessageBox.Ok, QMessageBox.Ok)
            return

        No_Of_Posts_To_Make=int(No_Of_Posts_To_Make_str)
        #QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + UserName+Password+Delay, QMessageBox.Ok, QMessageBox.Ok)
