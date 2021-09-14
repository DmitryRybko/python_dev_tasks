from PyQt5.QtWidgets import QWidget, qApp, QApplication, QMainWindow, QFileDialog
from PyQt5 import uic
import sys
import sqlite3
from sqlite3 import Error


class Window(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = uic.loadUi('desktop_app.ui', self)

    def btn_select_db_clicked(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*)",
                                                  options=options)
        if filename:
            print(f'Открыта база данных: {filename}')
            self.ui.textBrowser_2.setText(filename)
            conn = None
            try:
                conn = sqlite3.connect(filename)
                print(f'соединение с бд установлено')
                try:
                    c = conn.cursor()
                    c.execute(""" CREATE TABLE IF NOT EXISTS categories (
                                        category_name text PRIMARY KEY,
                                        category_description text NOT NULL
                                    ); """)
                except Error as e:
                    print(e)
            except Error as e:
                print(e)

    def menu_categories_clicked(self):
        print("test")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())


# def create_connection(db_file):
#
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         print(f'соединение с бд установлено')
#         return conn
#     except Error as e:
#         print(e)
#     return conn
