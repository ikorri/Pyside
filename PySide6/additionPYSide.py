import re

regex = re.compile(r"^[0-9]+")
res = re.findall(regex, "Bonjour 111 Aurevoir 222")

import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog,QLabel,QHBoxLayout,QMessageBox)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.setWindowTitle('Addition')
        self.label1 = QLabel("1er nombre  : ")
        self.label2 = QLabel("2ème nombre:")
        self.label3 = QLabel("La somme des deux nombre = ")
        self.label4 = QLabel(".......")

        self.edit1 = QLineEdit("")
        self.edit1.setPlaceholderText("Saisir un nombre entier")
        self.edit2 = QLineEdit()
        self.edit2.setPlaceholderText("Saisir un nombre entier")
        # self.edit2.setEchoMode((QLineEdit.Password))
        
        self.button = QPushButton("Calculer")
        self.button2 = QPushButton("Effacer")
        self.button3 = QPushButton("Quitter")
        # self.button2.hide()
        # Create layout and add widgets
        layoutVer = QVBoxLayout()
        layoutHor1 = QHBoxLayout()
        layoutHor2 = QHBoxLayout()
        layoutHor3 = QHBoxLayout()
        layoutHor4 = QHBoxLayout()

        layoutHor1.addWidget(self.label1)
        layoutHor1.addWidget(self.edit1)

        layoutHor2.addWidget(self.label2)
        layoutHor2.addWidget(self.edit2)

        layoutHor3.addWidget(self.button)
        layoutHor3.addWidget(self.button2)
        layoutHor4.addWidget(self.label3)
        layoutHor4.addWidget(self.label4)



        # layoutVer.addWidget(self.edit2)
        layoutVer.addLayout(layoutHor1)
        layoutVer.addLayout(layoutHor2)
        layoutVer.addLayout(layoutHor3)
        layoutVer.addLayout(layoutHor4)
        layoutVer.addWidget(self.button3)
        # layoutVer.addWidget(self.label3)

        # Set dialog layout
        self.setLayout(layoutVer)

        # Add button signal to greetings slot
        self.button.clicked.connect(self.calculer)
        self.button2.clicked.connect(self.effacer)
        self.button3.clicked.connect(quit)
        self.messagebox = QMessageBox()
        self.messagebox.setText("Erreur de saisie")

    # Greets the user
    def calculer(self):
        try:
            nb1  = int(self.edit1.text())
            nb2  = int(self.edit2.text())
        except:
            self.messagebox.show()
            self.effacer()
        
        else:
            resulat = str(nb1 + nb2)
            self.label4.setText(resulat)



        # print(f"Hello {self.edit1.text()}")
            
            # self.button.setText("Se déconnecter")

            # self.edit1.setPlaceholderText("Enter Username Here")
            # self.edit2.setPlaceholderText("Enter Password Here")
            # self.button.hide()
            # self.label1.hide()
            # self.label2.hide()
            # self.edit1.hide()
            # self.edit2.hide()
            # self.button2.show()
            
            
        # else:
        #     self.edit1.setText("")
        #     self.edit2.setText("")
        #     self.messagebox.show()

    def effacer(self):
        
        # print(f"Hello {self.edit1.text()}")
        self.label4.setText("")
        self.edit1.setText("")
        self.edit2.setText("")
        # self.edit1.setPlaceholderText("Enter Username Here")
        # self.edit2.setPlaceholderText("Enter Password Here") 
        # self.button.setText("Se déconnecter")

        # self.label1.show()
        # self.label2.show()
        # self.edit1.show()
        # self.edit2.show()
        # self.button.show()
        # self.button2.hide()
        

            
            
            

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())