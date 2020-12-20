import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from random import randint
from PIL import Image
from math import factorial
import pyperclip


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Interface.ui', self)  # Загружаем дизайн
        self.outsideImage.clicked.connect(self.give_image_to_encrypt)
        self.outsideText.clicked.connect(self.give_text)
        # self.saveImage.clicked.connect(self.get_image)
        self.upload.clicked.connect(self.give_image_to_decrypt)
        self.encryptedText.setReadOnly(True)
        self.generator.clicked.connect(self.generate_key)
        # self.encryptedText.setText('Hello World!!!')
        self.downloadImage.clicked.connect(self.text_save)
        self.saveImage.clicked.connect(self.image_save)
        self.copy.clicked.connect(self.copy_password)
        self.paste.clicked.connect(self.paste_password)

    def give_image_to_encrypt(self):
        self.image_name = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '', 'Картинка (*.bmp)')[
            0]
        self.pixmap = QPixmap(self.image_name)

        self.userImage.setPixmap(self.pixmap)

    def give_image_to_decrypt(self):
        self.decrypt_name = \
            QFileDialog.getOpenFileName(self, 'Choose picture', '',
                                        'Картинка (*.bmp)')[0]
        self.pixmap1 = QPixmap(self.decrypt_name)
        self.decryptImage.setPixmap(self.pixmap1)

    def give_text(self):
        text_name = QFileDialog.getOpenFileName(self, 'Choose text', '',
                                                'Текст (*.txt);;Текст (*.docx);;Текст (*.rtf)')[0]
        with open(text_name) as file:
            text = file.read()
            self.plainTextEdit.insertPlainText(text)

    def text_save(self):
        path = QFileDialog.getSaveFileName(self, 'Save file', '', 'Текст (*.txt);;Текст (*.docx);;Текст (*.rtf)')[0]
        with open(path, 'w') as file:
            text = self.encryptedText.toPlainText()
            file.write(text)

    def image_save(self):
        path = \
            QFileDialog.getSaveFileName(self, 'Save file', '', 'Картинка (*.bmp)')[0]
        # im.save(path)

    def generate_key(self):
        try:
            x = self.pixmap.width()
            y = self.pixmap.height()
            chars = 100  # количество символов в тексте
            self.keyout.setText(str(randint(0, factorial(x * y) // (factorial(x * y - chars)))))
        except AttributeError:
            QMessageBox.critical(self, "Error!", "Сначала выберите картинку и введите текст для шифровки")

    def copy_password(self):
        pyperclip.copy(self.keyout.text())

    def paste_password(self):
        self.decryptkey.setText(pyperclip.paste())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
