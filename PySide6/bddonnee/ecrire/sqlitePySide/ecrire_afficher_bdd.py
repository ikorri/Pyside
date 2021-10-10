import sys, os.path
from PySide6 import QtWidgets, QtGui, QtSql
import sqlite3
import operator
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QMessageBox
# from PySide6 import QtWidgets



# h = 300
# l = 400
 
# mybdd = 'myBdd'

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
        self.txt1 = QtWidgets.QLineEdit("",self)
        self.layoutHor1 = QtWidgets.QHBoxLayout()
        self.layoutHor1.addWidget(txt)
        self.layoutHor1.addWidget(self.txt1)

        txt1 = QtWidgets.QLabel("Prénom", self)
        self.txt2 = QtWidgets.QLineEdit("",self)
        self.layoutHor2 = QtWidgets.QHBoxLayout()
        self.layoutHor2.addWidget(txt1)
        self.layoutHor2.addWidget(self.txt2)
        
        self.btn = QtWidgets.QPushButton("Enregistrer", self)
        self.btn.clicked.connect(self.action)
        self.btn2 = QtWidgets.QPushButton("Afficher", self)
        self.btn2.clicked.connect(self.afficher)
        self.layoutHor3 = QtWidgets.QHBoxLayout()
        self.layoutHor3.addWidget(self.btn)
        self.layoutHor3.addWidget(self.btn2)

        self.btn1 = QtWidgets.QPushButton("Quitter", self)
        self.btn1.clicked.connect(quit)
        self.layoutHor4 = QtWidgets.QHBoxLayout()
        self.layoutHor4.addWidget(self.btn1)

        # self.table_model = MyTableModel(self, data_list, header)
        # self.table_view = QtWidgets.QTableView()
        # self.table_view.setModel(self.table_model)
        # # set font
        # font = QFont("Courier New", 14)
        # self.table_view.setFont(font)
        # # set column width to fit contents (set font first!)
        # self.table_view.resizeColumnsToContents()
        # # enable sorting
        # self.table_view.setSortingEnabled(True)

        self.layout = QtWidgets.QVBoxLayout(self)
        # self.layout2 = QtWidgets.QHBoxLayout(self)
        self.layoutHor5 = QtWidgets.QHBoxLayout()
        # self.layoutHor5.addWidget(self.table_view)
        self.layout.addLayout(self.layoutHor1)
        self.layout.addLayout(self.layoutHor2)
        self.layout.addLayout(self.layoutHor3)
        self.layout.addLayout(self.layoutHor4)
        self.layout.addLayout(self.layoutHor5)

        self.messagebox = QMessageBox()
        self.messagebox.setText("Attention! Au moins un champ est vide")
        
        conn = sqlite3.connect("tadatabase.db")
        c = conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS employee
        (
            nom text,
            prenom text       
        )
        """)
        if self.txt2.text()=="" or self.txt1.text()=="":
            print("Champs vide")
            
            pass
        else:
            d = {"prenom":self.txt2.text(),"nom":self.txt1.text()}
            c.execute("INSERT INTO employee VALUES(:prenom,:nom)",d)

            conn.commit()
            conn.close()
        
        # self.setLayout(self.layout)
        # self.setLayout(self.layout2)

        self.conn = sqlite3.connect("tadatabase.db")
        c = self.conn.cursor()
        c.execute("SELECT * FROM employee")
        data_list = c.fetchall()
        self.conn.commit()
        self.conn.close()
        header = ['Nom', ' Prénom']
        self.table_model = MyTableModel(self, data_list, header)
        self.table_view = QtWidgets.QTableView()
        self.table_view.setModel(self.table_model)
        
    # def __del__(self):
    #     pass


    def misAjour(self):
        self.table_view.setModel(None)
        self.table_view.hide()
        self.conn = sqlite3.connect("tadatabase.db")
        c = self.conn.cursor()
        c.execute("SELECT * FROM employee")
        data_list = c.fetchall()
        self.conn.commit()
        self.conn.close()

        self.table_model = MyTableModel(self, data_list, header)
        self.table_view = QtWidgets.QTableView()
        self.table_view.setModel(self.table_model)
        # set font
        font = QFont("Courier New", 14)
        self.table_view.setFont(font)
        # set column width to fit contents (set font first!)
        self.table_view.resizeColumnsToContents()
        # enable sorting
        self.table_view.setSortingEnabled(True)

        

        self.layoutHor5.addWidget(self.table_view)
        # header2 = ['Name', ' Lastname']
        # self.table_model2 = MyTableModel(self, data_list2, header2)
        # self.table_view2 = QtWidgets.QTableView()
          

        # self.table_view2.setModel(self.table_model2)

        # font = QFont("Courier New", 14)
        # self.table_view2.setFont(font)
        # # set column width to fit contents (set font first!)
        # self.table_view.resizeColumnsToContents()
        # # enable sorting
        # self.table_view2.setSortingEnabled(True)
        # self.layout.addWidget(self.table_view2)
        # self.table_view.hide()
        self.setLayout(self.layout)

    

    def afficher(self):
        # self.table_view.setModel(None)
        
        self.misAjour()
        # self.table_view.hide()
        # self.conn = sqlite3.connect("madatabase.db")
        # c = self.conn.cursor()
        # c.execute("SELECT * FROM employee")
        # data_list = c.fetchall()
        # print(data_list)
        # self.header = ['Nom', ' Prénom']
        # use numbers for numeric data to sort properly
        # conn = sqlite3.connect("madatabase.db")
        # c = conn.cursor()
        # c.execute("SELECT * FROM employee")
        # self.data_list = c.fetchall()
        # conn.commit()
        # conn.close()

        # self.deleteLater()
        # app2 = QtWidgets.QApplication([])
        # win2 = MyWindow(data_list, header)
        
        # win2.show()
        # sys.exit(app2.exec())
        # self.deleteLater(self.layout)
        # self.clearLayout(self.layout)
        
        # self.table_view.setModel(None)

        # self.conn = sqlite3.connect("madatabase.db")
        # c = self.conn.cursor()
        # c.execute("SELECT * FROM employee")
        # data_list2 = c.fetchall()
        # self.conn.commit()
        # self.conn.close()

        # header2 = ['Name', ' Lastname']
        # self.table_model2 = MyTableModel(self, data_list2, header2)
        # self.table_view2 = QtWidgets.QTableView()
          

        # self.table_view2.setModel(self.table_model2)

        # font = QFont("Courier New", 14)
        # self.table_view2.setFont(font)
        # # set column width to fit contents (set font first!)
        # self.table_view.resizeColumnsToContents()
        # # enable sorting
        # self.table_view2.setSortingEnabled(True)
        # self.layout.addWidget(self.table_view2)
        # self.table_view.hide()
        # self.setLayout(self.layout)

        



        
        # self.table_view.destroy(destroyWindow=True,destroySubWindows=True)

        # self.setupUi()
        # self.table_model = MyTableModel(self, data_list, header)
        # self.table_view = QtWidgets.QTableView()
        # self.table_view.setModel(self.table_model)
        
        # self.setLayout(self.layout)

        



        

        
        # pass
        
    def action(self):
        # liste = [self.txt1.text(), self.txt2.text()]

        self.conn = sqlite3.connect("tadatabase.db")
        c = self.conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS employee
        (
            nom text,
            prenom text       
        )
        """)
        if self.txt2.text()=="" or self.txt1.text()=="":
            print("Champs vide")
            self.messagebox.show()
        else:
            d = {"prenom":self.txt2.text(),"nom":self.txt1.text()}
            c.execute("INSERT INTO employee VALUES(:nom,:prenom)",d)

        self.conn.commit()
        self.conn.close()

        self.txt1.setText("")
        self.txt2.setText("")
        # font = QFont("Courier New", 14)
        # self.table_view.setFont(font)
        # # set column width to fit contents (set font first!)
        # self.table_view.resizeColumnsToContents()
        # # enable sorting
        # self.table_view.setSortingEnabled(True)
        # self.table_view.setModel(self.table_model)
    
    # def clearLayout(self, layout):
    #     if layout is not None:
    #         while layout.count():
    #             item = layout.takeAt(0)
    #             widget = item.widget()
    #             if widget is not None:
    #                 widget.deleteLater()
    #             else:
    #                 self.clearLayout(item.layout())
            
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


# conn = sqlite3.connect("tadatabase.db")
# c = conn.cursor()
# c.execute("""
# CREATE TABLE IF NOT EXISTS employee
# (
#     nom text,
#     prenom text       
# )
# """)
# conn.commit()
# conn.close()

 
header = ['Nom', ' Prénom']
# use numbers for numeric data to sort properly
conn = sqlite3.connect("tadatabase.db")
c = conn.cursor()
c.execute("SELECT * FROM employee")
# data_list = c.fetchall()
conn.commit()
conn.close()

# app = QtWidgets.QApplication(sys.argv)
# frame = Frame()
# frame.show()

app = QtWidgets.QApplication([])
win = MyWindow([], header)
# win2 = MyWindow(data_list, header)
# win2.setWindowTitle("Bis")
# win2.hide()
win.show()
sys.exit(app.exec())





