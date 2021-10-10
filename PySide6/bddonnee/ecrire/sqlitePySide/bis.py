import sys, os.path
from PySide6 import QtWidgets, QtGui, QtSql
import sqlite3
import operator
from PySide6.QtCore import *
from PySide6.QtGui import *
# from PySide6 import QtWidgets



h = 300
l = 400
 
mybdd = 'myBdd'

# class Frame(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         ## Création de la fenêtre.
#         QtWidgets.QMainWindow.__init__(self, parent)

class MyWindow(QtWidgets.QWidget):
    def __init__(self, data_list, header, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi()
    
    def setupUi(self):
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(300, 200, 570, 450)
        self.setWindowTitle("Click on column title to sort")

    
        txt = QtWidgets.QLabel("Nom", self)
        # txt.move(10, 10)
        self.txt1 = QtWidgets.QLineEdit("",self)

        layoutHor1 = QtWidgets.QHBoxLayout()
        layoutHor1.addWidget(txt)
        layoutHor1.addWidget(self.txt1)

        # self.txt1.move(100,10)
        txt1 = QtWidgets.QLabel("Prénom", self)
        # txt1.move(10, 50)
        self.txt2 = QtWidgets.QLineEdit("",self)
        # self.txt2.move(100,50)

        layoutHor2 = QtWidgets.QHBoxLayout()
        layoutHor2.addWidget(txt1)
        layoutHor2.addWidget(self.txt2)
        
        self.btn = QtWidgets.QPushButton("Enregistrer", self)
        # self.btn.move(10, 100)
        self.btn.clicked.connect(self.action)

        self.btn2 = QtWidgets.QPushButton("Afficher", self)
        # self.btn2.move(200, 150)
        self.btn2.clicked.connect(self.afficher)


        layoutHor3 = QtWidgets.QHBoxLayout()
        layoutHor3.addWidget(self.btn)
        layoutHor3.addWidget(self.btn2)

        

        self.btn1 = QtWidgets.QPushButton("Quitter", self)
        # self.btn1.move(200, 100)
        self.btn1.clicked.connect(quit)

        layoutHor4 = QtWidgets.QHBoxLayout()
        layoutHor4.addWidget(self.btn1)

        


        table_model = MyTableModel(self, data_list, header)
        table_view = QtWidgets.QTableView()
        table_view.setModel(table_model)
        # set font
        font = QFont("Courier New", 14)
        table_view.setFont(font)
        # set column width to fit contents (set font first!)
        table_view.resizeColumnsToContents()
        # enable sorting
        table_view.setSortingEnabled(True)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addLayout(layoutHor1)
        self.layout.addLayout(layoutHor2)
        self.layout.addLayout(layoutHor3)
        self.layout.addLayout(layoutHor4)
        self.layout.addWidget(table_view)
        self.setLayout(self.layout)

        conn = sqlite3.connect("madatabase.db")
        c = conn.cursor()
        c.execute("SELECT * FROM employee")
        self.data_list = c.fetchall()
        conn.commit()
        conn.close()
    def __del__(layout):
        pass
    def afficher(self):
        # self.conn = sqlite3.connect("madatabase.db")
        # c = self.conn.cursor()
        # c.execute("SELECT * FROM employee")
        # data_list = c.fetchall()
        # print(data_list)


        # self.deleteLater(self.layout)
        # self.layout.deleteLater()
        pass

        # self.conn.commit()
        # self.conn.close()
        
    def action(self):
        # liste = [self.txt1.text(), self.txt2.text()]

        self.conn = sqlite3.connect("madatabase.db")
        c = self.conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS employee
        (
            prenom text,
            nom text
        )
        """)
        if self.txt2.text()=="" or self.txt1.text()=="":
            print("Champs vide")
            pass
        else:
            d = {"prenom":self.txt2.text(),"nom":self.txt1.text()}
            c.execute("INSERT INTO employee VALUES(:prenom,:nom)",d)

            self.conn.commit()
            self.conn.close()

        self.txt1.setText("")
        self.txt2.setText("")
        

class MyTableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header
    def rowCount(self, parent):
        return len(self.mylist)
    def columnCount(self, parent):
        return len(self.mylist[0])
    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None
    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.mylist = sorted(self.mylist,
            key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(SIGNAL("layoutChanged()"))


 
header = ['Nom', ' Prénom']
# use numbers for numeric data to sort properly
conn = sqlite3.connect("madatabase.db")
c = conn.cursor()
c.execute("SELECT * FROM employee")
data_list = c.fetchall()
conn.commit()
conn.close()


# app = QtWidgets.QApplication(sys.argv)
# frame = Frame()
# frame.show()

app = QtWidgets.QApplication([])
win = MyWindow(data_list, header)

win.show()
sys.exit(app.exec())