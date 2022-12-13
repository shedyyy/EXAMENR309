#https://github.com/shedyyy/EXAMENR309

import sys
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMainWindow, QComboBox, QGridLayout, QMessageBox, QTextBrowser, QTextEdit
import socket

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)

        self.setWindowTitle("Le serveur de tchat")
        self.lbl = QLabel(self)
        self.lbl.setText("Serveur")
        self.champ = QLineEdit(self)
        self.champ3 = QLineEdit(self)
        self.bouton = QPushButton(self)
        self.bouton.setText("Démarrage du serveur")
        self.bouton.clicked.connect(self.demarrage)

        self.lbl2 = QLabel(self)
        self.lbl2.setText("Port")
        self.champ2 = QLineEdit(self)
        self.lbl3 = QLabel(self)
        self.lbl3.setText("Nombre de clients maximum")

        self.affichage = QTextEdit(self)
        self.affichage.setReadOnly(True)

        grid.addWidget(self.lbl, 2, 1)
        grid.addWidget(self.champ, 2, 2)
        grid.addWidget(self.champ3, 4, 2)
        grid.addWidget(self.bouton, 5, 1)
        grid.addWidget(self.lbl2, 3, 1)
        grid.addWidget(self.lbl3, 4, 1)
        grid.addWidget(self.champ2, 3, 2)
        grid.addWidget(self.affichage, 6,1,2,7)

    def demarrage(self):
        host = localhost
        port = 10000
        server_socket = socket.socket()
        server_socket.bind((host, port))
        server_socket.listen(5)



if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()