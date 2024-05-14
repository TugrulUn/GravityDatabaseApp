from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("Developer")

        self.setFixedWidth(300)
        self.setFixedHeight(250)

        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("GRAVITY ROBOTIC")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        label_pic = QLabel()
        pixmap = QPixmap('gravity.png')
        pixmap = pixmap.scaledToWidth(200)
        label_pic.setPixmap(pixmap)
        label_pic.setFixedHeight(200)

        layout.addWidget(title)
        # layout.addWidget(QLabel("Version 5.3.2"))
        # layout.addWidget(QLabel("Copyright 2018 CYB Inc."))
        layout.addWidget(label_pic)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)