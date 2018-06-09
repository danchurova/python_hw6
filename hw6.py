#!/usr/bin/env python3

import sys
import numpy as np
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import GEOparse
import pandas as pd
from scipy import stats

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
        genes=genesEdit.text().split(',')
        gse = GEOparse.get_GEO(geo='GSE'+str(gseEdit.text()), destdir= './')
        for gsm_name, gsm in gse.gsms.items():
            print("Name: ", gsm_name)
            print("Metadata:",)
            for key, value in gsm.metadata.items():
                print(" - %s : %s" % (key, ", ".join(value)))
            print ("Table data:",)
            print (gsm.table.head())
            break
        # p_val = stats.ks_2samp()[1]

        # p_value.setText("p-value: "+ str(p_val)[:3])
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

