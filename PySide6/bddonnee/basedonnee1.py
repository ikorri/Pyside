import sys, os.path
from PySide6 import QtSql,QtWidgets,QtGui

# from PySide6 import QtCore, QtGui, QtSql

from PySide6.QtWidgets import (QWidget, QLabel, QLineEdit, QSizePolicy,
    QHBoxLayout, QApplication,)
 
h = 300
l = 400
 
class Frame(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        ## Création de la fenêtre.
        QtWidgets.QMainWindow.__init__(self, parent)
        self.resize(l,h)
        self.setFont(QtGui.QFont("Verdana"))
        self.setWindowTitle("Bases de données")
 
        #Création de la basse de données
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE") ## Nous indiquons ici le driver avec lequel nous souhaitons travailler. 
        ## Les driver permettent de définir avec quel type de bases de données nous allons travailler. 
        ## Notez qu'il en existe un grand nombre et qu'il vous est même possible d'en personnaliser. Mais ceci sort du contexte actuel.
        self.db.setDatabaseName('myBdd') ## Nous nommons ici notre base de données.
        self.db.open() ## Commande permettant d'accéder à la base de données
        
        query = QtSql.QSqlQuery()
        query.exec('''create table Contact (id INTEGER PRIMARY KEY,nom TEXT, prenom TEXT)''') 
        ## Création de la table Contact dans notre base de données ouverte.
        self.db.commit() ## Enregistrement de la base de données
        self.db.close() ## Fermeture de celle-ci
 
app = QtWidgets.QApplication(sys.argv)
frame = Frame()
frame.show()
sys.exit(app.exec())