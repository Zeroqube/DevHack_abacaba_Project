import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Interface.ui', self)  # Загружаем дизайн
        self.outsideImage.clicked.connect(self.convert)
        self.outsideText.clicked.connect(self.get_text)
        self.saveImage.clicked.connect(self.get_image)

    def convert(self):
        self.image_name = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '', 'Картинка (*.jpg);;Все файлы (*)')[
            0]
        self.pixmap = QPixmap(self.image_name)
        self.userImage.setPixmap(self.pixmap)

    def get_text(self):
        text_name = QFileDialog.getOpenFileName(self, 'Выбрать текст', '', 'Текст (*.txt);;Все файлы (*)')[0]
        with open(text_name) as file:
            text = file.read()
            self.plainTextEdit.insertPlainText(text)

    def get_image(self):
        # image = ''  # picture after encrypting
        # res_im = QPixmap(image)
        # self.resultImage.setPixmap(res_im)
        self.resultImage.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
