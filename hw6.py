#!/usr/bin/env python3

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import GEOparse

def main():

    app = QApplication(sys.argv) #ignore()
    window = QWidget()
    window.setWindowTitle("Hello World")
    window.show()

    # [Add widgets to the widget]

    # Create some widgets (these won't appear immediately):
    p_value = QLabel("p-value:")
    gseLabel = QLabel("GSE Number:")
    gseEdit = QLineEdit()
    genesLabel = QLabel("Signalling pathway genes names:")
    genesEdit = QLineEdit()
    def on_click():
        p_value.setText("value")
    button = QPushButton('Search')
    button.setToolTip('This is an example button')
    button.clicked.connect(on_click)


    # Put the widgets in a layout (now they start to appear):
    layout = QGridLayout(window)
    layout.addWidget(gseLabel, 0, 0)
    layout.addWidget(gseEdit, 0, 1)
    layout.addWidget(genesLabel, 1, 0)
    layout.addWidget(genesEdit, 1, 1)
    layout.addWidget(button, 2, 0)
    layout.addWidget(p_value, 2, 1)
    # layout.setRowStretch(2, 1)


    # [Resizing the window]

    # Let's resize the window:
    window.resize(480, 160)


    # [Run the application]

    # Start the event loop...
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
