import sys, os.path
from PySide6 import QtWidgets, QtGui, QtSql
import sqlite3

h = 300
l = 400
 
mybdd = 'myBdd'
 
class Frame(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        ## Création de la fenêtre.
        QtWidgets.QMainWindow.__init__(self, parent)
        self.resize(l,h)
        self.setFont(QtGui.QFont("Verdana"))
        self.setWindowTitle("Bases de données")
    
        txt = QtWidgets.QLabel("Nom", self)
        txt.move(10, 10)
        self.txt1 = QtWidgets.QLineEdit("",self)
        self.txt1.move(100,10)
        txt1 = QtWidgets.QLabel(u"Prénom", self)
        txt1.move(10, 50)
        self.txt2 = QtWidgets.QLineEdit("",self)
        self.txt2.move(100,50)
        
        self.btn = QtWidgets.QPushButton("Enregistrer", self)
        self.btn.move(10, 100)
        self.btn.clicked.connect(self.action)

        self.btn1 = QtWidgets.QPushButton("Quitter", self)
        self.btn1.move(200, 100)
        self.btn1.clicked.connect(quit)

        self.btn2 = QtWidgets.QPushButton("Afficher", self)
        self.btn2.move(200, 150)
        self.btn2.clicked.connect(self.afficher)

        self.label1 =QtWidgets.QLabel("1",self)
        self.label1.move(30, 200)
        self.label2 =QtWidgets.QLabel("2",self)
        self.label2.move(150, 200)
        self.label3 =QtWidgets.QLabel("1",self)
        self.label3.move(30, 220)
        self.label4 =QtWidgets.QLabel("2",self)
        self.label4.move(150, 220)


    def afficher(self):
        self.conn = sqlite3.connect("madatabase.db")
        c = self.conn.cursor()
        c.execute("SELECT * FROM employee")
        donnees = c.fetchall()
        print(donnees)
        
        self.label1.setText(donnees[-2][0])
        self.label2.setText(donnees[-2][1])
        self.label3.setText(donnees[-1][0])
        self.label4.setText(donnees[-1][1])

        self.conn.commit()
        self.conn.close()
        



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

        # Écriture dans dans la basse de données
        ## Les six lignes ci-dessous permettent de se connecter à la base de données et de sélectionner la table dans laquelle on souhaite travailler
        # self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        # self.db.setDatabaseName(mybdd)
        # self.db.open()
        # self.model = QtSql.QSqlTableModel()
        # self.model.setTable("Contact")
        # self.model.select()
        # ## On insère une ligne supplémentaire qui sera remplie par la suite. Si cette ligne de code est oubliée, c'est une modification qui sera effectuée.
        # self.model.insertRows(0, 1)
        # a = 0
        # ## Nous créons une boucle permettant de rentrer les valeurs des QLineEdit dans notre base de données
        # while a <= 1:
        #     ## setData() requiert en premier argument l'index de la ligne à créer, en deuxième la valeur.
        #     ## Ici dans le premier argument a+1 correspond à la deuxième colonne de notre table si a = 0. On laisse la première colonne se remplir seule (clé automatique).
        #     ## Le premier argument de self.model.index peut prendre n'importe quelle valeur. Ceci ne change rien.
        #     self.model.setData(self.model.index(0, a+1), liste[a])
        #     a+=1
        # self.model.submitAll() ## cette commande permet de sauvegarder les modifications effectuées dans la table.
        # self.db.close() ## On ferme la base de données.
 
 
app = QtWidgets.QApplication(sys.argv)
frame = Frame()
frame.show()
sys.exit(app.exec())