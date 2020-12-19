import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Interface.ui', self)  # Загружаем дизайн
        self.outsideImage.clicked.connect(self.convert)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def convert(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        print(fname)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
