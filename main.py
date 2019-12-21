from sys import argv, exit
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.Qt import Qt
import sqlite3
from os.path import isfile


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        if isfile("./coffee.sqlite"):
            self.db = sqlite3.connect("coffee.sqlite")
        else:
            self.show_messagebox("Database error!")
            exit()
        self.initUi()
        self.update_table()

    def initUi(self):
        uic.loadUi("main.ui", self)
        self.action_exit.triggered.connect(exit)

    def clear_table(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)

    def create_cursor(self):
        self.cur = self.db.cursor()

    def execute_query(self, query):
        return self.cur.execute(query)

    def execute_query_fetchone(self, query):
        return self.cur.execute(query).fetchone()

    def close_cursor(self):
        self.cur.close()

    def get_col_names(self):
        self.create_cursor()
        self.execute_query_fetchone("SELECT * FROM coffee")
        names = map(lambda val: val[0], self.cur.description)
        self.close_cursor()
        return tuple(names)

    def show_messagebox(self, message):
        msgbox = QMessageBox(self)
        msgbox.setText(message)
        msgbox.show()

    def fill_table(self, header, data):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setColumnCount(len(header))
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableWidget.setRowCount(0)
        for row_num, row_data in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for el_num, el in enumerate(row_data):
                item = QTableWidgetItem(str(el))
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                self.tableWidget.setItem(row_num, el_num, item)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def update_table(self):
        header = self.get_col_names()
        self.create_cursor()
        data = list(self.execute_query(f"SELECT * FROM coffee"))
        data = [list(row) for row in data]
        replacements = {"type": "types", "taste": "tastes"}
        for row in data:
            for repl_el, repl_tab in replacements.items():
                row_id = header.index(repl_el)
                repl_id = row[row_id]
                new_el = self.execute_query_fetchone(
                    f"SELECT {repl_el} FROM {repl_tab} WHERE id='{repl_id}'")
                if new_el is not None:
                    row[row_id] = new_el[0]
        self.fill_table(header, data)
        self.close_cursor()


def main():
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()
