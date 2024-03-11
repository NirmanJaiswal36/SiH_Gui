from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("sample_gui.ui", self)
        self.show()

        self.login.clicked.connect(self.login)
    
    def login(self):
        if self.username.text()=="nirman" and self.password.text()=="password":
            self.textEdit.setEnabled(True)
            self.pushButton.setEnabled(True)
        else:
            message = QMessageBox()
            message.setText("Invalid Login")
            message.exec_()

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == "__main__":
    main()