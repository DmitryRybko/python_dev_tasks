import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication


class CatalogMainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.menu_bar = self.menuBar()

        self.gma_menu = self.menu_bar.addMenu('Основное меню')
        self.categories_open_btn = QAction(self)
        self.categories_open_btn.setText('категории')
        self.employees_open_btn = QAction(self)
        self.employees_open_btn.setText('сотрудники')
        self.goods_open_btn = QAction(self)
        self.goods_open_btn.setText('товары')

        self.positions_open_btn = QAction(self)
        self.positions_open_btn.setText('должности')
        self.units_open_btn = QAction(self)
        self.units_open_btn.setText('единицы измерения')
        self.vendors_open_btn = QAction(self)
        self.vendors_open_btn.setText('поставщики')

        self.gma_menu.addAction(self.categories_open_btn)
        self.gma_menu.addAction(self.employees_open_btn)
        self.gma_menu.addAction(self.goods_open_btn)
        self.gma_menu.addAction(self.positions_open_btn)
        self.gma_menu.addAction(self.units_open_btn)
        self.gma_menu.addAction(self.vendors_open_btn)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    CMW = CatalogMainWindow()
    CMW.setWindowTitle('Складской учет')
    CMW.setFixedSize(1200, 800)
    CMW.show()
    sys.exit(app.exec_())