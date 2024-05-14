from PySide2 import QtGui
from PySide2.QtWidgets import QDialog, QLineEdit, QVBoxLayout, QPushButton, QLabel, QMessageBox, QComboBox

class CommentDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(CommentDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(500)
        self.setFixedHeight(320)

        layout = QVBoxLayout()


        self.addButton = QPushButton()
        self.addButton.setText("Yorumu Ekle")
        self.setWindowTitle('Comment')
        self.setWindowIcon(QtGui.QIcon('logo.jpeg'))
        self.addButton.clicked.connect(self.ekle)

        CommentString = QLineEdit(self)
        CommentString.setEchoMode(QLineEdit.Password)
        CommentString.setPlaceholderText("Enter Your Comment.")
        CommentString.setFixedWidth(480)
        CommentString.setFixedHeight(200)

        Code = QLabel("774101")
        Name = QLabel("BEARING UNIT UCP-201, SHAFT DIAM 12MM")
        font1 = Code.font()
        font1.setPointSize(16)
        Code.setFont(font1)

        font2 = Name.font()
        font2.setPointSize(16)
        Name.setFont(font2)

        layout.addWidget(Code)
        layout.addWidget(Name)
        layout.addWidget(CommentString)
        layout.addWidget(self.addButton)
        self.setLayout(layout)

    def ekle(self):
        pass