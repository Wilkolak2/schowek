import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.text = ""
        self.ui.pasteBtn.clicked.connect(self.paste)
        self.ui.copyBtn.clicked.connect(self.copy)

    def copy(self):
        self.text = self.ui.value1.text()

    def paste(self):
        self.ui.value2.setText(self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())
