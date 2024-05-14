from PySide2 import QtGui
from PySide2.QtWidgets import QDialog, QVBoxLayout, QPushButton, QHBoxLayout, QListWidget

class ComponyDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(ComponyDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(1300)
        self.setFixedHeight(600)
        self.setWindowTitle('Company Interface')
        self.setWindowIcon(QtGui.QIcon('logo.jpeg'))

        # file_menu = self.menuBar().addMenu("&Anasayfa")
        # help_menu = self.menuBar().addMenu("&About")

        v1layout = QHBoxLayout()
        v2layout = QHBoxLayout()
        hlayout = QVBoxLayout()

        btn1 = QPushButton("Spare Parts")
        v1layout.addWidget(btn1)

        btn2 = QPushButton("IMPA")
        v1layout.addWidget(btn2)

        btn3 = QPushButton("Lubrication")
        v1layout.addWidget(btn3)

        btn4 = QPushButton("Chemicals")
        v1layout.addWidget(btn4)

        self.listbox1 = QListWidget()
        self.listbox1.addItem("297 - Adjusting screw - Fuel Injection Valve - NICO - 2 Adet")
        self.listbox1.addItem("544 - Air piston - Fuel Pump - 3 Adet")
        self.listbox1.addItem("248 - Atomizer, complete - Fuel Pump - 1 Adet")
        self.listbox1.addItem("602 - Ball bearing (1) - Horizontal Shaft - 6 Adet")
        self.listbox1.addItem("487 - Bushing - Connecting Rod and Crosshead - 4 Adet")
        v2layout.addWidget(self.listbox1)

        self.listbox2 = QListWidget()
        self.listbox2.addItem("15 01 01 - White 1,370x2300 - 3 Adet")
        self.listbox2.addItem("774101 - BEARING UNIT UCP-201, SHAFT DIAM 12MM - 6 Adet")
        self.listbox2.addItem("710401 - PIPE CARBONSTEEL HIGH-PRESSURE, STS SCH-40 1/8(6A)X5.5MTR - 2 Adet")
        v2layout.addWidget(self.listbox2)

        self.listbox3 = QListWidget()
        self.listbox3.addItem("GulfSea SuperBear 3008 - 1 Adet")
        self.listbox3.addItem("Prista SuperBear 3008 - 4 Adet")
        self.listbox3.addItem("ATLANTA MARINE D 3005 - 4 Adet")
        self.listbox3.addItem("ENERGOL OE-HT 30 - 7 Adet")
        self.listbox3.addItem("Energol DL-MP 30 - 3 Adet")
        v2layout.addWidget(self.listbox3)

        self.listbox4 = QListWidget()
        self.listbox4.addItem("B.W.T. New Formula - 4 Adet")
        self.listbox4.addItem("Boiler Sludge Conditioner - 1 Adet")
        self.listbox4.addItem("Oxygen Scavenger Plus - 8 Adet")
        self.listbox4.addItem("Liquid Coagulant - 2 Adet")
        self.listbox4.addItem("Alkalinity Control - 3 Adet")
        v2layout.addWidget(self.listbox4)

        hlayout.addLayout(v1layout)
        hlayout.addLayout(v2layout)
        self.setLayout(hlayout)

    def ekle(self):
        pass