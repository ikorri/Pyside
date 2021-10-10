import sys, os.path
from PySide6 import QtWidgets, QtGui, QtSql
import sqlite3
import operator
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QMessageBox

class MyWindow(QtWidgets.QWidget): # Constructeur
    def __init__(self, data_list, header, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi() # Appel de la méthode setupUi()
    
    def setupUi(self): # Définition de la méthde setupUi()
        # setGeometry(x_pos, y_pos, width, height) Position de la fenetre
        self.setGeometry(300, 200, 570, 450)
        self.setWindowTitle("Click on column title to sort") # Titre de l'application

    
        lbl_Nom = QtWidgets.QLabel("Nom", self)
        self.lEdit_Nom = QtWidgets.QLineEdit("",self)
        self.layoutHor1 = QtWidgets.QHBoxLayout()
        self.layoutHor1.addWidget(lbl_Nom)
        self.layoutHor1.addWidget(self.lEdit_Nom)

        lbl_Prenom = QtWidgets.QLabel("Prénom", self)
        self.lEdit_Prenom = QtWidgets.QLineEdit("",self)
        self.layoutHor2 = QtWidgets.QHBoxLayout()
        self.layoutHor2.addWidget(lbl_Prenom)
        self.layoutHor2.addWidget(self.lEdit_Prenom)
        
        self.btn_Enregistrer = QtWidgets.QPushButton("Enregistrer", self)
        self.btn_Enregistrer.clicked.connect(self.action)
        self.btn_Afficher = QtWidgets.QPushButton("Afficher", self)
        self.btn_Afficher.clicked.connect(self.afficher)
        self.layoutHor3 = QtWidgets.QHBoxLayout()
        self.layoutHor3.addWidget(self.btn_Enregistrer)
        self.layoutHor3.addWidget(self.btn_Afficher)

        self.btn_Quitter = QtWidgets.QPushButton("Quitter", self)
        self.btn_Quitter.clicked.connect(quit)
        self.layoutHor4 = QtWidgets.QHBoxLayout()
        self.layoutHor4.addWidget(self.btn_Quitter)


        self.layout = QtWidgets.QVBoxLayout(self)
        
        self.layoutHor5 = QtWidgets.QHBoxLayout()
    
        self.layout.addLayout(self.layoutHor1)
        self.layout.addLayout(self.layoutHor2)
        self.layout.addLayout(self.layoutHor3)
        self.layout.addLayout(self.layoutHor4)
        self.layout.addLayout(self.layoutHor5)

        self.messagebox = QMessageBox()
        self.messagebox.setText("Attention! Au moins un champ est vide")

    # creer un ebases de donne Appel de fonction
        self.creer_bdd()

        data_list = self.selectionner_donnee()

        # self.conn = sqlite3.connect("sadatabase.db")
        # c = self.conn.cursor()
        # c.execute("SELECT * FROM employee")
        # data_list = c.fetchall()
        # self.conn.commit()
        # self.conn.close()

        header = ['Nom', ' Prénom']
        self.table_model = MyTableModel(self, data_list, header)
        self.table_view = QtWidgets.QTableView()
        self.table_view.setModel(self.table_model)

    def selectionner_donnee(self):
        self.conn = sqlite3.connect("sadatabase.db")
        c = self.conn.cursor()
        c.execute("SELECT * FROM employee")
        data_list = c.fetchall()
        self.conn.commit()
        self.conn.close()
        return data_list  
        
    def misAjour(self):
        self.table_view.setModel(None)
        self.table_view.hide()

        data_list = self.selectionner_donnee()

        # self.conn = sqlite3.connect("sadatabase.db")
        # c = self.conn.cursor()
        # c.execute("SELECT * FROM employee")
        # data_list = c.fetchall()
        # self.conn.commit()
        # self.conn.close()

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
        self.setLayout(self.layout)

    

    def afficher(self):
        
        self.misAjour()
        
        
    def action(self):
        # liste = [self.lEdit_Nom.text(), self.lEdit_Prenom.text()]
        self.creer_bdd()
        # self.conn = sqlite3.connect("sadatabase.db")
        # c = self.conn.cursor()
        # c.execute("""
        # CREATE TABLE IF NOT EXISTS employee
        # (
        #     nom text,
        #     prenom text       
        # )
        # """)
        # if self.lEdit_Prenom.text()=="" or self.lEdit_Nom.text()=="":
        #     print("Champs vide")
        #     self.messagebox.show()
        # else:
        #     d = {"prenom":self.lEdit_Prenom.text(),"nom":self.lEdit_Nom.text()}
        #     c.execute("INSERT INTO employee VALUES(:nom,:prenom)",d)

        # self.conn.commit()
        # self.conn.close()

        self.lEdit_Nom.setText("")
        self.lEdit_Prenom.setText("")
        self.afficher()

    def creer_bdd(self):    
        self.conn = sqlite3.connect("sadatabase.db")
        c = self.conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS employee
        (
            nom text,
            prenom text       
        )
        """)
        if self.lEdit_Prenom.text()=="" or self.lEdit_Nom.text()=="":
            print("Champs vide")
            
        else:
            d = {"prenom":self.lEdit_Prenom.text(),"nom":self.lEdit_Nom.text()}
            c.execute("INSERT INTO employee VALUES(:nom,:prenom)",d)
            self.conn.commit()
            self.conn.close()
                   
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
# conn = sqlite3.connect("sadatabase.db")
# c = conn.cursor()
# c.execute("SELECT * FROM employee")
# # data_list = c.fetchall()
# conn.commit()
# conn.close()

# app = QtWidgets.QApplication(sys.argv)
# frame = Frame()
# frame.show()

app = QtWidgets.QApplication([])
win = MyWindow([("","")], header)
win.show()
sys.exit(app.exec())





