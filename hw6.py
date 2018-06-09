#!/usr/bin/env python3

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import GEOparse

def main():

    app = QApplication(sys.argv) #ignore()
    window = QWidget()
    window.setWindowTitle("Gene Expression Omnibus Database GUI")
    window.show()


    p_value = QLabel("p-value:")
    gseLabel = QLabel("GSE Number:")
    gseEdit = QLineEdit()
    genesLabel = QLabel("Signalling pathway genes names:")
    genesEdit = QLineEdit()
    def on_click():
        print(gseEdit.text())
        gse = GEOparse.get_GEO(geo='GSE'+str(gseEdit.text()), destdir= './')
        print(gse.phenotype_data)
        p_value.setText("value")
    button = QPushButton('Search')
    button.setToolTip('This is an example button')
    button.clicked.connect(on_click)


    layout = QGridLayout(window)
    layout.addWidget(gseLabel, 0, 0)
    layout.addWidget(gseEdit, 0, 1)
    layout.addWidget(genesLabel, 1, 0)
    layout.addWidget(genesEdit, 1, 1)
    layout.addWidget(button, 2, 0)
    layout.addWidget(p_value, 2, 1)



    window.resize(480, 160)



    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

