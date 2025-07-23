import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot

from desing import Ui_MainWindow

class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabButton1.clicked.connect(self.switchToFifth)
        self.ui.tabButton2.clicked.connect(self.switchToThird)
        self.ui.tabButton3.clicked.connect(self.switchToSecond)
        self.ui.tabButton4.clicked.connect(self.switchToFirst)
        self.ui.tabButton5.clicked.connect(self.switchToFourth)
    @Slot()
    def switchToFirst(self):
        self.ui.tabWidget.setCurrentIndex(0)
    def switchToSecond(self):
        self.ui.tabWidget.setCurrentIndex(1)
    def switchToThird(self):
        self.ui.tabWidget.setCurrentIndex(2)
    def switchToFourth(self):
        self.ui.tabWidget.setCurrentIndex(3)
    def switchToFifth(self):
        self.ui.tabWidget.setCurrentIndex(4)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())
