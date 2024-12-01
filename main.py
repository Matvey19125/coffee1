import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QHeaderView
from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.coffetable.setVisible(False)
        self.clicked.clicked.connect(self.active)

    def active(self):
        self.coffetable.setVisible(True)
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee')
        if not db.open():
            return
        model = QSqlQueryModel()
        query = "SELECT * FROM coffee"
        model.setQuery(query)
        if model.lastError().isValid():
            return
        self.coffetable.setModel(model)
        header = self.coffetable.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())