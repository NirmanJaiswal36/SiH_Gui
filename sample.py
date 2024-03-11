from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

def main():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("My Simple GUI")
    window.setGeometry(500,500,500,400)

    layout = QVBoxLayout(window)
    label = QLabel("Press the Button Below")
    textbox = QTextEdit()
    button = QPushButton("Press here")
    button.clicked.connect(lambda: on_clicked(textbox.toPlainText()))

    #window.setLayout(layout)

    layout.addWidget(label)
    layout.addWidget(textbox)
    layout.addWidget(button)

    window.show()
    app.exec_()

def on_clicked(msg):
    message = QMessageBox()
    message.setText(msg)
    message.exec_()
    print("Hello world")
     

if __name__== "__main__":
    main()
