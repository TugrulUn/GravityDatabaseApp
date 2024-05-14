from PySide2 import QtGui, QtCore
from PySide2.QtWidgets import QDialog, QLineEdit, QVBoxLayout, QPushButton, QLabel, QMessageBox, QGridLayout
from PySide2.QtGui import QColor, QPalette, QFont


class LoginDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(LoginDialog, self).__init__(*args, **kwargs)

        # self.setFixedWidth(1600)
        # self.setFixedHeight(900)

        self.left = 200
        self.top = 50
        self.title = 'Login'
        self.width = 1600
        self.height = 900
        self.initUI()
        # self.passbutton = QPushButton()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon('logo.jpeg'))
        self.setGeometry(self.left, self.top, self.width, self.height)

        passlabel = QLabel(self)
        passlabel.setText("Login")
        passlabel.setFont(QFont('Times', 90))
        passlabel.move(30, 500)

        passinput = QLineEdit(self)
        passinput.setEchoMode(QLineEdit.Password)
        passinput.setPlaceholderText("Enter Password.")
        passinput.setFixedWidth(600)
        passinput.setFixedHeight(30)
        passinput.move(30, 700)

        self.passbutton = QPushButton(self)
        self.passbutton.setText("Login")
        self.passbutton.setFont(QFont('Times', 15))
        self.passbutton.setFixedWidth(600)
        self.passbutton.setFixedHeight(30)
        self.passbutton.move(30, 750)
        self.passbutton.clicked.connect(self.login)

        self.setStyleSheet(
            "QWidget {background-image: url(loginImage.jpeg); background-repeat: no-repeat; background-position: center}")

        self.show()



        # layout = QVBoxLayout()
        # grid = QGridLayout()
        #
        # self.passinput = QLineEdit()
        # self.passinput.setEchoMode(QLineEdit.Password)
        # self.passinput.setPlaceholderText("Enter Password.")
        # self.QBtn = QPushButton()
        # self.QBtn.setText("Login")
        # self.setWindowTitle('Login')
        # self.QBtn.clicked.connect(self.login)
        #
        # # self.passinput.setGeometry(850, 20, 100, 20)
        # self.passinput.move(200, 200)
        # # title = QLabel("Login")
        # # font = title.font()
        # # font.setPointSize(16)
        # # title.setFont(font)
        # label =QLabel("       ")
        #
        # # layout.addWidget(title)
        # # layout.addWidget(self.passinput)
        # # layout.addWidget(self.QBtn)
        # # self.setLayout(layout)
        #
        # grid.addWidget(self.passinput, 2, 0)
        # grid.addWidget(self.QBtn, 3, 0)
        # grid.addWidget(label, 2, 1)
        # self.setLayout(grid)



    def login(self):
        if(self.passinput.text() == ""):
            self.accept()
        else:
            QMessageBox.warning(self, 'Error', 'Wrong Password')
