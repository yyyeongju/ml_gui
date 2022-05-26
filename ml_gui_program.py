from PyQt5.QtWidgets import *
import sys,pickle
from PyQt5 import uic, QtWidgets ,QtCore, QtGui
from data_visualise import data_

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('mainwindow.ui',self)

        global data, steps
        data =data_()


        self.Browse = self.findChild(QPushButton, "Browse")
        self.columns = self.findChild(QListWidget, "colum_list")
        self.Browse.clicked.connect(self.getCSV)
    
    def filldetails(self, flag=1):
        if flag == 0:
            self.df = data.read_file(str(self.filePath))
        
        #self.columns.clear()
        self.columns_list = data.get_column_list(self.df)
        print(self.columns_list)

        for i , j in enumerate(self.columns_list):
            #print (i,j)
            stri = f"{j}------{str(self.df[j].dtype)}"
            #print(stri)
            self.columns.insertItem(i, stri)


    def getCSV(self):
        self.filePath , _= QtWidgets.QFileDialog.getOpenFileName(self, "Open file", "", "csv(*.csv)")
        #self.columns.clear()
        print(self.filePath)
        if self.filePath !="":
            self.filldetails(0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    window.show()

    sys.exit(app.exec_())