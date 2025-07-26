import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt
from PySide6.QtCore import QSize
from desing import Ui_MainWindow
from desing import count
from cleaning.temp import clean_directory
from optimization.browser import disable_edge
from optimization.cortana import disable_cortana
from optimization.perfomance import performance_mode
from optimization.update import disable_windows_updates
from optimization.xboxGB import disable_xbox_game_bar
from tweaks.context_menu import restore_win10_context_menu

import os

script = []
temp_default = 'C:/Windows/temp'
temp_with_percent = os.environ.get('TEMP')
class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(QSize(898, 637))
        self.setWindowTitle("Crystal")
        self.count = count
        self.ui.tabButton1.clicked.connect(self.switchToFifth)
        self.ui.tabButton2.clicked.connect(self.switchToThird)
        self.ui.tabButton3.clicked.connect(self.switchToSecond)
        self.ui.tabButton4.clicked.connect(self.switchToFirst)
        self.ui.tabButton5.clicked.connect(self.switchToFourth)
        self.ui.checkBox.checkStateChanged.connect(self.check_state)
        self.ui.checkBox_2.checkStateChanged.connect(self.check_state)
        self.ui.checkBox_3.checkStateChanged.connect(self.check_state)
        self.ui.checkBox_4.checkStateChanged.connect(self.check_state)
        self.ui.checkBox_5.checkStateChanged.connect(self.check_state)
        self.ui.checkBox_6.checkStateChanged.connect(self.check_state)
        self.ui.checkBox_7.checkStateChanged.connect(self.check_state)
        self.ui.checkBox_8.checkStateChanged.connect(self.check_state)
        self.ui.checkBox_9.checkStateChanged.connect(self.check_state)
        self.ui.checkBox_10.checkStateChanged.connect(self.check_state)
        self.ui.checkBox_12.checkStateChanged.connect(self.check_state)
    def check_state(self, status):
        if status == Qt.CheckState.Checked:
            self.count += 1
            self.ui.label_2.setText(f"\u0427\u0438\u0441\u043b\u043e \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0445 \u0432\u0430\u043c\u0438 \u0444\u0443\u043d\u043a\u0446\u0438\u0439: {self.count}")
        elif status == Qt.CheckState.Unchecked and self.count > 0:
            self.count -= 1
            self.ui.label_2.setText(f"\u0427\u0438\u0441\u043b\u043e \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0445 \u0432\u0430\u043c\u0438 \u0444\u0443\u043d\u043a\u0446\u0438\u0439: {self.count}")
    @Slot()
    def switchToFirst(self):
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.label_3.setText("Crystal ➜ Home")
    def switchToSecond(self):
        self.ui.tabWidget.setCurrentIndex(1)
        self.ui.label_3.setText("Crystal ➜ Clean")
    def switchToThird(self):
        self.ui.tabWidget.setCurrentIndex(2)
        self.ui.label_3.setText("Crystal ➜ Optimization")
    def switchToFourth(self):
        self.ui.tabWidget.setCurrentIndex(3)
        self.ui.label_3.setText("Crystal ➜ Tweaks")
    def switchToFifth(self):
        self.ui.tabWidget.setCurrentIndex(4)
        self.ui.label_3.setText("Crystal ➜ Personalize")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())
