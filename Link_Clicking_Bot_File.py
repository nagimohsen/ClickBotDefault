# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Link_Clicking_Bot_File.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from MainFile import Link_Click
from PyQt5.QtCore import pyqtSlot, QThread, Qt
from PyQt5.QtGui import QIcon, QGuiApplication
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout,
                             QGroupBox, QHBoxLayout, QComboBox, QLineEdit, QMessageBox, QLabel, QProgressBar, QTextEdit,
                             QCheckBox, QSizePolicy)
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 431, 521))
        font = QtGui.QFont()
        font.setFamily("Lemon")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.Proxies_List = QtWidgets.QListWidget(self.groupBox)
        self.Proxies_List.setGeometry(QtCore.QRect(10, 60, 151, 401))
        self.Proxies_List.setObjectName("Proxies_List")
        self.Delete_Selected_Proxy_btn = QtWidgets.QPushButton(self.groupBox)
        self.Delete_Selected_Proxy_btn.setGeometry(QtCore.QRect(10, 470, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Lemon")
        self.Delete_Selected_Proxy_btn.setFont(font)
        self.Delete_Selected_Proxy_btn.setObjectName("Delete_Selected_Proxy_btn")
        self.Use_Proxies_check_box = QtWidgets.QCheckBox(self.groupBox)
        self.Use_Proxies_check_box.setGeometry(QtCore.QRect(10, 30, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Lemon")
        self.Use_Proxies_check_box.setFont(font)
        self.Use_Proxies_check_box.setObjectName("Use_Proxies_check_box")
        self.Add_Proxy_edtxt = QtWidgets.QLineEdit(self.groupBox)
        self.Add_Proxy_edtxt.setGeometry(QtCore.QRect(190, 60, 231, 31))
        self.Add_Proxy_edtxt.setObjectName("Add_Proxy_edtxt")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(190, 40, 111, 16))
        self.label.setObjectName("label")
        self.click_to_Add_Proxy_btn = QtWidgets.QPushButton(self.groupBox)
        self.click_to_Add_Proxy_btn.setGeometry(QtCore.QRect(270, 110, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Lemon")
        self.click_to_Add_Proxy_btn.setFont(font)
        self.click_to_Add_Proxy_btn.setStyleSheet("")
        self.click_to_Add_Proxy_btn.setObjectName("click_to_Add_Proxy_btn")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(510, 10, 261, 200))
        font = QtGui.QFont()
        font.setFamily("Lemon")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")

        self.Add_your_Link_Here_edtxt = QtWidgets.QLineEdit(self.groupBox_2)
        self.Add_your_Link_Here_edtxt.setGeometry(QtCore.QRect(10, 70, 231, 31))
        self.Add_your_Link_Here_edtxt.setObjectName("Add_your_Link_Here_edtxt")

        self.Add_amount_edtxt = QtWidgets.QLineEdit(self.groupBox_2)
        self.Add_amount_edtxt.setGeometry(QtCore.QRect(10, 150, 231, 31))
        self.Add_amount_edtxt.setObjectName("Amount_of_clicks_edtxt")



        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 171, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 171, 16))
        self.label_3.setObjectName("label_2")

        self.Start_Bot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Start_Bot_btn.setGeometry(QtCore.QRect(630, 470, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Lemon")
        self.Start_Bot_btn.setFont(font)
        self.Start_Bot_btn.setObjectName("Start_Bot_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuThis_a_Link_Clicking_Bot = QtWidgets.QMenu(self.menubar)
        self.menuThis_a_Link_Clicking_Bot.setObjectName("menuThis_a_Link_Clicking_Bot")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuThis_a_Link_Clicking_Bot.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.Link_Click_obj=Link_Click()
        self.Proxies_List.addItems(self.Link_Click_obj.Load_Data_From())
        #self.Start_Bot_btn.clicked.connect(self.Link_Click_obj.Start_Bot)
        self.click_to_Add_Proxy_btn.clicked.connect(self.click_to_Add_Proxy_btn_click_event)
        self.Delete_Selected_Proxy_btn.clicked.connect(self.Delete_Selected_Proxy_btn_click_btn_event)
        self.Start_Bot_btn.clicked.connect(self.Start_Bot_btn_click_event)
        

    def Delete_Selected_Proxy_btn_click_btn_event(self):
        try:
            proxy=[str(x.text()) for x in self.Proxies_List.selectedItems()][0]
        except Exception as e:
            if 'list index out of range' in str(e):
                print('nothing to delete!!!!!!!!')
                return
        
        for item in self.Proxies_List.selectedItems():
            self.Proxies_List.takeItem(self.Proxies_List.row(item))
        self.Link_Click_obj.RemoveProxy(proxy)

        
    
    def click_to_Add_Proxy_btn_click_event(self):
        proxy=self.Add_Proxy_edtxt.text()
        proxy=proxy.strip()


        items = []
        for index in range(self.Proxies_List.count()):
            items.append(self.Proxies_List.item(index).text().strip())
        if items.__contains__(proxy):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("cannot allow duplicate proxies")
            msg.setWindowTitle("Warning")
            msg.setDetailedText("You are entering a \nproxy that already exists!!!!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            retval = msg.exec_()                    # <<<---- !!!

            print("value of pressed message box button:", retval)
            return


        if proxy=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Enter a valid proxy and\nthen press this button")
            msg.setWindowTitle("MessageBox demo")
            msg.setDetailedText("You have to enter valid proxy in\nAdd Proxy Edit Text")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            retval = msg.exec_()                    # <<<---- !!!

            print("value of pressed message box button:", retval)
        else:
            self.Proxies_List.addItem(proxy)
            self.Link_Click_obj.Add_Proxy(proxy)

    def Start_Bot_btn_click_event(self):
        link=self.Add_your_Link_Here_edtxt.text()
        no_of_clicks=0
        try:
            if (self.Add_amount_edtxt.text())=='':
                no_of_clicks=0
            else:
                no_of_clicks=int(self.Add_amount_edtxt.text())
            print(no_of_clicks)
        except Exception as e:
            print("\n\nCould Not Convert in digit\n\n"+str(e))
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("In the click amount edtxt please enter a valid digit")
            msg.setWindowTitle("Not A digit in click amount!!!!!")
            msg.setDetailedText("In Click amount The only thing you can add is a number\nno spaces,no latters no special characters are allowed!!!")

            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()                    # <<<---- !!!

            print("value of pressed message box button:", retval)
            return
        


        link=link.strip()
        if link=='':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Enter a valid link and\nthen press this button")
            msg.setWindowTitle("Link Error")
            msg.setDetailedText("You have to enter valid link in\nAdd Proxy Edit Text")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            retval = msg.exec_()                    # <<<---- !!!

            print("value of pressed message box button:", retval)
        else:
            items = []
            for index in range(self.Proxies_List.count()):
                items.append(self.Proxies_List.item(index).text().strip())
            if len(items)==0 and self.Use_Proxies_check_box.isChecked():
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You have no proxies in the list\nand you have checked to use proxies")
                msg.setWindowTitle("0 Proxies")
                msg.setDetailedText("you are trying to use an empty proxies list , that is invalid use\nWhen you have no proxies in the list\nyou can uncheck the use proxy checkbox\nand use your original ip address to browse the link:)")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
                retval = msg.exec_()                    # <<<---- !!!
                return
            self.Link_Click_obj.Start_Bot(link,items,self.Use_Proxies_check_box.isChecked(),no_of_clicks)
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Link Clicking Bot"))
        self.groupBox.setTitle(_translate("MainWindow", "Proxy Management Section"))
        self.Delete_Selected_Proxy_btn.setText(_translate("MainWindow", "Delete Selected proxy"))
        self.Use_Proxies_check_box.setText(_translate("MainWindow", "Use Proxies"))
        self.label.setText(_translate("MainWindow", "Add Proxy"))
        self.click_to_Add_Proxy_btn.setText(_translate("MainWindow", "Click to Add Proxy"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Link Management Section"))
        self.label_2.setText(_translate("MainWindow", "Please Enter A Valid Link"))

        self.label_3.setText(_translate("MainWindow", "Enter Amount of clicks"))
        self.Start_Bot_btn.setText(_translate("MainWindow", "Start Bot"))
        self.menuThis_a_Link_Clicking_Bot.setTitle(_translate("MainWindow", "This a Link Clicking Bot"))


if __name__ == "__main__":
    '''conn = sqlite3.connect("ProxiesDB.db") # or use :memory: to put it in RAM

    cursor = conn.cursor()

    # create a table
    cursor.execute("""CREATE TABLE Proxies_List
                  (Proxies text) 
               """)'''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
