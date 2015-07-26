#!/usr/bin/env python3
import sys
from PySide import QtGui

from ui import Ui_Form

class MainForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.exit(app.exec_())

        
