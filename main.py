import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt
from PySide6.QtCore import QSize
from desing import Ui_MainWindow
from desing import count
from functions.cleaning.temp import clean
from functions.optimization.browser import disable_edge
from functions.optimization.cortana import disable_cortana
from functions.optimization.perfomance import performance_mode
from functions.optimization.update import disable_windows_updates
from functions.optimization.xboxGB import disable_xbox_game_bar
from functions.tweaks.context_menu import restore_win10_context_menu
from functions.personalize.switchTheme import switchThemeToLight, switchThemeToDark
import os

from Logs.log import clog, set_main_window
from Parsing.jsonParser import add7zipToScript, addFirefoxToScript, addVSCodeToScript, executeScript

# Пути для очистки
temp_default_path = 'C:/Windows/temp'
temp_with_percent_path = os.environ.get('TEMP')
yandex_cache_path = os.path.join(os.environ['LOCALAPPDATA'], 'Yandex', 'YandexBrowser', 'User Data', 'Default', 'Cache')
chrome_cache_path = os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'Chrome', 'User Data', 'Default', 'Cache')
update_windows_cache_path = 'C:/Windows/SoftwareDistribution/Download'
prefetch_path = 'C:/Windows/Prefetch'

class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        set_main_window(self)
        self.setFixedSize(QSize(790, 637))
        self.setWindowTitle("Crystal")
        self.ui.textEdit.setReadOnly(True)
        self.count = count
        
        # Очередь для выбранных функций
        self.function_queue = []
        
        # Привязываем кнопки переключения вкладок
        self.ui.tabButton1.clicked.connect(self.switchToFifth)
        self.ui.tabButton2.clicked.connect(self.switchToThird)
        self.ui.tabButton3.clicked.connect(self.switchToSecond)
        self.ui.tabButton4.clicked.connect(self.switchToFirst)
        self.ui.tabButton5.clicked.connect(self.switchToFourth)
        self.ui.pushButton_3.clicked.connect(self.switchToSixth)
        self.ui.pushButton_4.clicked.connect(self.switchToSeventh)
        # Привязываем чекбоксы
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
        
        # Привязываем кнопку для выполнения всех выбранных функций
        self.ui.pushButton.clicked.connect(self.execute_functions)
        self.ui.pushButton_8.clicked.connect(executeScript)

        self.ui.add7zip.clicked.connect(add7zipToScript)
        self.ui.addFirefox.clicked.connect(addFirefoxToScript)
        self.ui.addVSCode.clicked.connect(addVSCodeToScript)

        self.ui.darkTheme.clicked.connect(lambda: switchThemeToDark(self))
        self.ui.lightTheme.clicked.connect(lambda: switchThemeToLight(self))

    def check_state(self, status):
        if status == Qt.CheckState.Checked:
            if self.sender() == self.ui.checkBox:
                func = lambda: clean(temp_default_path)
                self.function_queue.append(func)
                self.sender().setProperty("stored_func", func)
            elif self.sender() == self.ui.checkBox_2:
                func = lambda: clean(update_windows_cache_path)
                self.function_queue.append(func)
                self.sender().setProperty("stored_func", func)
            elif self.sender() == self.ui.checkBox_3:
                func = lambda: clean(yandex_cache_path)
                self.function_queue.append(func)
                self.sender().setProperty("stored_func", func)
            elif self.sender() == self.ui.checkBox_4:
                func = lambda: clean(prefetch_path)
                self.function_queue.append(func)
                self.sender().setProperty("stored_func", func)
            elif self.sender() == self.ui.checkBox_5:
                func = lambda: clean(temp_with_percent_path)
                self.function_queue.append(func)
                self.sender().setProperty("stored_func", func)
            elif self.sender() == self.ui.checkBox_6:
                func = lambda: clean(disable_xbox_game_bar)
                self.function_queue.append(func)
                self.sender().setProperty("stored_func", func)
            elif self.sender() == self.ui.checkBox_7:
                func = lambda: clean(disable_windows_updates)
                self.function_queue.append(func)
                self.sender().setProperty("stored_func", func)
            elif self.sender() == self.ui.checkBox_8:
                func = lambda: clean(disable_cortana)
                self.function_queue.append(func)
                self.sender().setProperty("stored_func", func)
            elif self.sender() == self.ui.checkBox_9:
                func = lambda: clean(disable_edge)
                self.function_queue.append(func)
                self.sender().setProperty("stored_func", func)
            elif self.sender() == self.ui.checkBox_10:
                func = lambda: clean(performance_mode)
                self.function_queue.append(func)
                self.sender().setProperty("stored_func", func)
            elif self.sender() == self.ui.checkBox_12:
                func = lambda: clean(restore_win10_context_menu)
                self.function_queue.append(func)
                self.sender().setProperty("stored_func", func)

            self.count += 1
            self.ui.label_2.setText(f"{self.count}")
        
        elif status == Qt.CheckState.Unchecked and self.count > 0:
            # Убираем функцию из очереди, используя сохранённую функцию
            stored_func = self.sender().property("stored_func")
            if stored_func and stored_func in self.function_queue:
                self.function_queue.remove(stored_func)
            
            # Обновляем отображение количества выбранных функций
            self.count -= 1
            self.ui.label_2.setText(f"{self.count}")

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

    def switchToSixth(self):
        self.ui.tabWidget.setCurrentIndex(5)

    def switchToSeventh(self):
        self.ui.tabWidget.setCurrentIndex(6)
    @Slot()
    def execute_functions(self):
        # Выполняем все функции из очереди
        for func in self.function_queue:
            try:
                func()
            except Exception as e:
                clog(f"Ошибка при выполнении {func.__name__}: {e}")
        
        # Очищаем очередь после выполнения
        self.function_queue.clear()
        self.count = 0  # Сбрасываем счетчик
        self.ui.label_2.setText(f"{self.count}")
        
        clog("Все функции выполнены!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())