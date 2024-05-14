from PySide2.QtWidgets import QDialog, QLineEdit, QVBoxLayout, QPushButton, QLabel, QMessageBox, QComboBox

class IntroDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(IntroDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(300)
        self.setFixedHeight(120)

        layout = QVBoxLayout()

        self.adetCombo = QComboBox()
        self.adetCombo.addItems(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
        self.addButton = QPushButton()
        self.addButton.setText("Ekle")
        self.setWindowTitle('ORDER')
        self.addButton.clicked.connect(self.ekle)

        title = QLabel("SİPARİŞ VER")
        font = title.font()
        font.setPointSize(16)
        title.setFont(font)

        layout.addWidget(title)
        layout.addWidget(self.adetCombo)
        layout.addWidget(self.addButton)
        self.setLayout(layout)

    def ekle(self):
        print(self.adetCombo.currentText)