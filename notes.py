from PySide6.QtWidgets import QApplication, QFileDialog, QDialog
from Zametki import Ui_Dialog
import sys

class Base(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Заметки...")
        self.ui.Save.clicked.connect(self.Saved)
        self.ui.OpenF.clicked.connect(self.opens)
        self.ui.pushButton.clicked.connect(self.convectToPy)
    def Saved(self):
        self.t = self.ui.Text.toPlainText()
        files ,  _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Текстовые файлы (*.txt);;Все файлы (*.*)")
        if files:
            with open(files , "w", encoding="UTF-8") as file:
                file.write(self.t)
    def opens(self):
        files , _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Текстовые файлы (*.txt);;Все файлы (*.*)")
        if files:
            with open(files, "r", encoding="UTF-8") as file:
                self.con = file.read()
                self.ui.Text.setPlainText(self.con)
    def convectToPy(self):
        self.p = self.ui.Text.toPlainText()
        files ,  _ = QFileDialog.getSaveFileName(self, "Сохранить файл Python", "", "Python Files (*.py)")
        if files:
            with open(files , "w", encoding="UTF-8") as file:
                file.write(self.p)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    windw = Base()
    windw.show()
    sys.exit(app.exec())