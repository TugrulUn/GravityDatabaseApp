from PySide2.QtGui import QIntValidator
from PySide2.QtWidgets import QLineEdit
from sqlalchemy import create_engine, Column, Integer, String, BLOB, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import sys
from PySide2.QtCore import Qt, QSize
from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel
from colorpage import QColor
import sqlite3
from PySide2.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QTableView,
    QWidget,
    QPushButton,
    QToolBar,
    QStatusBar,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QGridLayout,
    QFormLayout, QMessageBox,
)

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("Yeni2.db")
db.open()


class FileEdit(QLineEdit):
    def __init__(self, parent):
        super(FileEdit, self).__init__(parent)

        self.setDragEnabled(True)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if (urls and urls[0].scheme() == 'file'):
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if (urls and urls[0].scheme() == 'file'):
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if (urls and urls[0].scheme() == 'file'):
            # for some reason, this doubles up the intro slash
            filepath = str(urls[0].path())[1:]
            self.setText(filepath)


class InsertWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Window")

        self.layout = QVBoxLayout()

        label = QLabel("Which table do you want to add?")
        robot_button = QPushButton("Robot")
        gorsel_button = QPushButton("Gorsel")
        hesapsal_button = QPushButton("Hesapsal")
        glink_file_button = QPushButton("Glink_File")
        hlink_file_button = QPushButton("Hlink_File")

        self.layout.addWidget(label)
        self.layout.addWidget(robot_button)
        self.layout.addWidget(gorsel_button)
        self.layout.addWidget(hesapsal_button)
        self.layout.addWidget(glink_file_button)
        self.layout.addWidget(hlink_file_button)

        robot_button.clicked.connect(self.onMyRobotInsertButtonClick)
        gorsel_button.clicked.connect(self.onMyGorselInsertButtonClick)
        hesapsal_button.clicked.connect(self.onMyHesapsalInsertButtonClick)
        glink_file_button.clicked.connect(self.onMyGlink_FileInsertButtonClick)
        hlink_file_button.clicked.connect(self.onMyHlink_FileInsertButtonClick)

        self.setLayout(self.layout)

    def onMyRobotInsertButtonClick(self, s):
        print("click", s)
        self.ri = RobotInsertWindow()
        self.ri.show()
        self.hide()
    def onMyGorselInsertButtonClick(self, s):
        print("click", s)
        self.gli = GorselInsertWindow()
        self.gli.show()
        self.hide()
    def onMyHesapsalInsertButtonClick(self, s):
        print("click", s)
        self.hli = HesapsalInsertWindow()
        self.hli.show()
        self.hide()
    def onMyGlink_FileInsertButtonClick(self, s):
        print("click", s)
        self.gfi = Glink_FileInsertWindow()
        self.gfi.show()
        self.hide()
    def onMyHlink_FileInsertButtonClick(self, s):
        print("click", s)
        self.hfi = Hlink_FileInsertWindow()
        self.hfi.show()
        self.hide()



class RobotInsertWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Robot Insert Window")
        layout = QVBoxLayout()
        self.label1 = QLabel("Robot Name:")
        self.name_input = QLineEdit()
        self.label2 = QLabel("Robot Type:")
        self.tip_input = QLineEdit()
        self.insert = QPushButton("Insert")
        self.insert.clicked.connect(self.action)
        layout.addWidget(self.label1)
        layout.addWidget(self.name_input)
        layout.addWidget(self.label2)
        layout.addWidget(self.tip_input)
        layout.addWidget(self.insert)
        self.setLayout(layout)

    def action(self):
        name = self.name_input.text()
        tip = self.tip_input.text()
        try:
            self.conn = sqlite3.connect("Yeni2.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO robot (robot_name, robot_tip) VALUES(?,?)", (name, tip))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Data is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add data to the database.')
        self.hide()

class GorselInsertWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gorsel Insert Window")
        layout = QVBoxLayout()
        self.label1 = QLabel("Link Numarası:")
        self.number_input = QLineEdit()
        self.label2 = QLabel("Gorsel Id:")
        self.id_input = QLineEdit()
        self.insert = QPushButton("Insert")
        self.insert.clicked.connect(self.action)
        layout.addWidget(self.label1)
        layout.addWidget(self.number_input)
        layout.addWidget(self.label2)
        layout.addWidget(self.id_input)
        layout.addWidget(self.insert)
        self.setLayout(layout)

    def action(self):
        number = self.number_input.text()
        gid = self.id_input.text()
        try:
            self.conn = sqlite3.connect("Yeni2.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO gorsel (link_number, robot_id) VALUES(?,?)", (number, gid))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Data is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add data to the database.')
        self.hide()

class HesapsalInsertWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hesapsal Insert Window")
        layout = QVBoxLayout()
        self.label1 = QLabel("Link Numarası:")
        self.number_input = QLineEdit()
        self.label2 = QLabel("Hesapsal Id:")
        self.id_input = QLineEdit()
        self.insert = QPushButton("Insert")
        self.insert.clicked.connect(self.action)
        layout.addWidget(self.label1)
        layout.addWidget(self.number_input)
        layout.addWidget(self.label2)
        layout.addWidget(self.id_input)
        layout.addWidget(self.insert)
        self.setLayout(layout)

    def action(self):
        number = self.number_input.text()
        hid = self.id_input.text()
        try:
            self.conn = sqlite3.connect("Yeni2.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO hesapsal (link_number, robot_id) VALUES(?,?)", (number, hid))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Data is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add data to the database.')
        self.hide()

class Glink_FileInsertWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Glink_File Insert Window")
        layout = QVBoxLayout()
        self.label1 = QLabel(".grm File:")
        self.grm_input = QLineEdit()
        self.label2 = QLabel(".step File:")
        self.step_input = QLineEdit()
        self.label3 = QLabel("Link Id:")
        self.id_input = QLineEdit()
        self.insert = QPushButton("Insert")

        self.dene1 = FileEdit(self.grm_input)
        self.dene2 = FileEdit(self.step_input)

        self.insert.clicked.connect(self.action)
        layout.addWidget(self.label1)
        layout.addWidget(self.grm_input)
        layout.addWidget(self.label2)
        layout.addWidget(self.step_input)
        layout.addWidget(self.label3)
        layout.addWidget(self.id_input)
        layout.addWidget(self.insert)
        self.setLayout(layout)



    def action(self):
        with open(self.dene1.text(), 'rb') as file:
            grmblobData = file.read()
        with open(self.dene2.text(), 'rb') as file:
            stepblobData = file.read()
        lid = self.id_input.text()
        try:
            self.conn = sqlite3.connect("Yeni2.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO glink_file (grmfile, stepfile, link_id) VALUES(?,?,?)", (grmblobData, stepblobData, lid))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Data is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add data to the database.')
        self.hide()


class Hlink_FileInsertWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hlink_File Insert Window")
        layout = QVBoxLayout()
        self.label1 = QLabel(".grm File:")
        self.grm_input = QLineEdit()
        self.label2 = QLabel(".step File:")
        self.step_input = QLineEdit()
        self.label3 = QLabel("Link Id:")
        self.id_input = QLineEdit()
        self.insert = QPushButton("Insert")
        self.insert.clicked.connect(self.action)
        layout.addWidget(self.label1)
        layout.addWidget(self.grm_input)
        layout.addWidget(self.label2)
        layout.addWidget(self.step_input)
        layout.addWidget(self.label3)
        layout.addWidget(self.id_input)
        layout.addWidget(self.insert)
        self.setLayout(layout)

    def action(self):
        grmfile = self.grm_input.text()
        stepfile = self.step_input.text()
        lid = self.id_input.text()
        try:
            self.conn = sqlite3.connect("Yeni2.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO hlink_file (grmfile, stepfile, slink_id) VALUES(?,?,?)",
                           (grmfile, stepfile, lid))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Data is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add data to the database.')
        self.hide()







class UpdateWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Window")
        self.layout = QVBoxLayout()

        label = QLabel("Which table do you want to update?")
        robot_button = QPushButton("Robot")
        gorsel_button = QPushButton("Gorsel")
        hesapsal_button = QPushButton("Hesapsal")
        glink_file_button = QPushButton("Glink_File")
        hlink_file_button = QPushButton("Hlink_File")

        self.layout.addWidget(label)
        self.layout.addWidget(robot_button)
        self.layout.addWidget(gorsel_button)
        self.layout.addWidget(hesapsal_button)
        self.layout.addWidget(glink_file_button)
        self.layout.addWidget(hlink_file_button)

        robot_button.clicked.connect(self.onMyRobotUpdateButtonClick)
        gorsel_button.clicked.connect(self.onMyGorselUpdateButtonClick)
        hesapsal_button.clicked.connect(self.onMyHesapsalUpdateButtonClick)
        glink_file_button.clicked.connect(self.onMyGlink_FileUpdateButtonClick)
        hlink_file_button.clicked.connect(self.onMyHlink_FileUpdateButtonClick)

        self.setLayout(self.layout)

    def onMyRobotUpdateButtonClick(self, s):
        print("click", s)
        self.ri = RobotUpdateWindow()
        self.ri.show()
        self.hide()
    def onMyGorselUpdateButtonClick(self, s):
        print("click", s)
        self.gli = GorselUpdateWindow()
        self.gli.show()
        self.hide()
    def onMyHesapsalUpdateButtonClick(self, s):
        print("click", s)
        self.hli = HesapsalUpdateWindow()
        self.hli.show()
        self.hide()
    def onMyGlink_FileUpdateButtonClick(self, s):
        print("click", s)
        self.gfi = Glink_FileUpdateWindow()
        self.gfi.show()
        self.hide()
    def onMyHlink_FileUpdateButtonClick(self, s):
        print("click", s)
        self.hfi = Hlink_FileInsertWindow()
        self.hfi.show()
        self.hide()

class RobotUpdateWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Robot Update Window")
        layout = QVBoxLayout()
        self.label1 = QLabel("Robot Name:")
        self.name_input = QLineEdit()
        self.label2 = QLabel("Robot Type:")
        self.tip_input = QLineEdit()
        self.insert = QPushButton("Insert")
        self.insert.clicked.connect(self.action)
        layout.addWidget(self.label1)
        layout.addWidget(self.name_input)
        layout.addWidget(self.label2)
        layout.addWidget(self.tip_input)
        layout.addWidget(self.insert)
        self.setLayout(layout)

    def action(self):
        name = self.name_input.text()
        # tip = self.tip_input.text()
        try:
            self.conn = sqlite3.connect("Yeni2.db")
            self.c = self.conn.cursor()
            # self.c.execute("Update robot set (robot_name=) WHERE robot_name="+str(name))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Data is updated successfully from table.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not update data from table.')
        self.hide()

class GorselUpdateWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gorsel Update Window")

class HesapsalUpdateWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hesapsal Update Window")

class Glink_FileUpdateWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Glink_File Update Window")

class Hlink_FileUpdateWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hlink_File Update Window")







class DeleteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Window")

        self.layout = QVBoxLayout()

        label = QLabel("From which table do you want to delete data?")
        robot_button = QPushButton("Robot")
        gorsel_button = QPushButton("Gorsel")
        hesapsal_button = QPushButton("Hesapsal")
        glink_file_button = QPushButton("Glink_File")
        hlink_file_button = QPushButton("Hlink_File")

        self.layout.addWidget(label)
        self.layout.addWidget(robot_button)
        self.layout.addWidget(gorsel_button)
        self.layout.addWidget(hesapsal_button)
        self.layout.addWidget(glink_file_button)
        self.layout.addWidget(hlink_file_button)

        robot_button.clicked.connect(self.onMyRobotDeleteButtonClick)
        gorsel_button.clicked.connect(self.onMyGorselDeleteButtonClick)
        hesapsal_button.clicked.connect(self.onMyHesapsalDeleteButtonClick)
        glink_file_button.clicked.connect(self.onMyGlink_FileDeleteButtonClick)
        hlink_file_button.clicked.connect(self.onMyHlink_FileDeleteButtonClick)

        self.setLayout(self.layout)

    def onMyRobotDeleteButtonClick(self, s):
        print("click", s)
        self.ri = RobotDeleteWindow()
        self.ri.show()
        self.hide()
    def onMyGorselDeleteButtonClick(self, s):
        print("click", s)
        self.gli = GorselDeleteWindow()
        self.gli.show()
        self.hide()
    def onMyHesapsalDeleteButtonClick(self, s):
        print("click", s)
        self.hli = HesapsalDeleteWindow()
        self.hli.show()
        self.hide()
    def onMyGlink_FileDeleteButtonClick(self, s):
        print("click", s)
        self.gfi = Glink_FileDeleteWindow()
        self.gfi.show()
        self.hide()
    def onMyHlink_FileDeleteButtonClick(self, s):
        print("click", s)
        self.hfi = Hlink_FileDeleteWindow()
        self.hfi.show()
        self.hide()

class RobotDeleteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gorsel Delete Window")

        layout = QVBoxLayout()
        self.label1 = QLabel("Data to be deleted:")
        self.name_input = QLineEdit()
        self.onlyInt = QIntValidator()
        self.name_input.setValidator(self.onlyInt)
        self.name_input.setPlaceholderText("Id.")
        self.insert = QPushButton("Delete")
        self.insert.clicked.connect(self.action)
        layout.addWidget(self.label1)
        layout.addWidget(self.name_input)
        layout.addWidget(self.insert)
        self.setLayout(layout)


    def action(self):
        delrol = self.name_input.text()

        try:
            self.conn = sqlite3.connect("Yeni2.db")
            self.c = self.conn.cursor()
            self.c.execute("DELETE from robot WHERE id="+str(delrol))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Data is deleted successfully from table.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not delete data from table.')
        self.hide()

class GorselDeleteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gorsel Delete Window")
        layout = QVBoxLayout()
        self.label1 = QLabel("Data to be deleted:")
        self.name_input = QLineEdit()
        self.onlyInt = QIntValidator()
        self.name_input.setValidator(self.onlyInt)
        self.name_input.setPlaceholderText("Id.")
        self.insert = QPushButton("Delete")
        self.insert.clicked.connect(self.action)
        layout.addWidget(self.label1)
        layout.addWidget(self.name_input)
        layout.addWidget(self.insert)
        self.setLayout(layout)

    def action(self):
        delrol = self.name_input.text()

        try:
            self.conn = sqlite3.connect("Yeni2.db")
            self.c = self.conn.cursor()
            self.c.execute("DELETE from gorsel WHERE id=" + str(delrol))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Data is deleted successfully from table.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not delete data from table.')
        self.hide()

class HesapsalDeleteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hesapsal Delete Window")
        layout = QVBoxLayout()
        self.label1 = QLabel("Data to be deleted:")
        self.name_input = QLineEdit()
        self.onlyInt = QIntValidator()
        self.name_input.setValidator(self.onlyInt)
        self.name_input.setPlaceholderText("Id.")
        self.insert = QPushButton("Delete")
        self.insert.clicked.connect(self.action)
        layout.addWidget(self.label1)
        layout.addWidget(self.name_input)
        layout.addWidget(self.insert)
        self.setLayout(layout)

    def action(self):
        delrol = self.name_input.text()

        try:
            self.conn = sqlite3.connect("Yeni2.db")
            self.c = self.conn.cursor()
            self.c.execute("DELETE from hesapsal WHERE id=" + str(delrol))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Data is deleted successfully from table.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not delete data from table.')
        self.hide()

class Glink_FileDeleteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Glink_File Delete Window")
        layout = QVBoxLayout()
        self.label1 = QLabel("Data to be deleted:")
        self.name_input = QLineEdit()
        self.onlyInt = QIntValidator()
        self.name_input.setValidator(self.onlyInt)
        self.name_input.setPlaceholderText("Id.")
        self.insert = QPushButton("Delete")
        self.insert.clicked.connect(self.action)
        layout.addWidget(self.label1)
        layout.addWidget(self.name_input)
        layout.addWidget(self.insert)
        self.setLayout(layout)

    def action(self):
        delrol = self.name_input.text()

        try:
            self.conn = sqlite3.connect("Yeni2.db")
            self.c = self.conn.cursor()
            self.c.execute("DELETE from glink_file WHERE id=" + str(delrol))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Data is deleted successfully from table.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not delete data from table.')
        self.hide()

class Hlink_FileDeleteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hlink_File Delete Window")
        layout = QVBoxLayout()
        self.label1 = QLabel("Data to be deleted:")
        self.name_input = QLineEdit()
        self.onlyInt = QIntValidator()
        self.name_input.setValidator(self.onlyInt)
        self.name_input.setPlaceholderText("Id.")
        self.insert = QPushButton("Delete")
        self.insert.clicked.connect(self.action)
        layout.addWidget(self.label1)
        layout.addWidget(self.name_input)
        layout.addWidget(self.insert)
        self.setLayout(layout)

    def action(self):
        delrol = self.name_input.text()

        try:
            self.conn = sqlite3.connect("Yeni2.db")
            self.c = self.conn.cursor()
            self.c.execute("DELETE from hlink_file WHERE id=" + str(delrol))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Data is deleted successfully from table.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not delete data from table.')
        self.hide()




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gravity Robotik Database")

        label = QLabel("Gravity Robotik")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        insert_button = QPushButton("Insert")
        update_button = QPushButton("Update")
        delete_button = QPushButton("Delete")

        insert_button.setStatusTip("If you click this button, the data will be added")
        update_button.setStatusTip("If you click this button the data will be updated")
        delete_button.setStatusTip("If you click this button, the data will be deleted.")

        insert_button.clicked.connect(self.onMyToolBarInsertButtonClick)
        update_button.clicked.connect(self.onMyToolBarUpdateButtonClick)
        delete_button.clicked.connect(self.onMyToolBarDeleteButtonClick)

        toolbar.addWidget(insert_button)
        toolbar.addWidget(update_button)
        toolbar.addWidget(delete_button)
        self.setStatusBar(QStatusBar(self))

        container = QWidget()

        layout = QGridLayout()

        self.listbox = QListWidget()
        self.listbox.addItems(["Robot", "Gorsel", "Hesapsal", "Glink_File", "Hlink_File"])

        self.listbox.currentTextChanged.connect(self.text_changed)

        self.search = QLineEdit()
        self.search.textChanged.connect(self.update_filter)

        self.table = QTableView()

        layout.addWidget(self.listbox, 0, 0, 0, 3)
        layout.addWidget(self.search, 0, 3, 1, 3)
        layout.addWidget(self.table, 1, 3, 1, 24)

        container.setLayout(layout)

        self.model = QSqlTableModel(db=db)
        self.table.setModel(self.model)
        self.model.setTable("robot")
        self.model.select()
        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(container)

    def onMyToolBarInsertButtonClick(self, s):
        print("click", s)
        self.i = InsertWindow()
        self.i.show()

    def onMyToolBarUpdateButtonClick(self, s):
        print("click", s)
        self.u = UpdateWindow()
        self.u.show()

    def onMyToolBarDeleteButtonClick(self, s):
        print("click", s)
        self.d = DeleteWindow()
        self.d.show()

    def update_filter(self, s):
        filter_str = 'Name LIKE "%{}%"'.format(s)
        self.model.setFilter(filter_str)

    def text_changed(self, s):
        self.model.setTable(s)
        self.model.select()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()



