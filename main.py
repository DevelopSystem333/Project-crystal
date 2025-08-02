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
import os

# Пути для очистки
temp_default = 'C:/Windows/temp'
temp_with_percent = os.environ.get('TEMP')
yandex_cache_path = os.path.join(os.environ['LOCALAPPDATA'], 'Yandex', 'YandexBrowser', 'User Data', 'Default', 'Cache')
chrome_cache_path = os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'Chrome', 'User Data', 'Default', 'Cache')

class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(QSize(790, 637))
        self.setWindowTitle("Crystal")
        self.count = count
        
        # Очередь для выбранных функций
        self.function_queue = []
        
        # Привязываем кнопки переключения вкладок
        self.ui.tabButton1.clicked.connect(self.switchToFifth)
        self.ui.tabButton2.clicked.connect(self.switchToThird)
        self.ui.tabButton3.clicked.connect(self.switchToSecond)
        self.ui.tabButton4.clicked.connect(self.switchToFirst)
        self.ui.tabButton5.clicked.connect(self.switchToFourth)

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
            
    def check_state(self, status):
        if status == Qt.CheckState.Checked:
            if self.sender() == self.ui.checkBox:
                self.function_queue.append(lambda: clean(temp_default))
            elif self.sender() == self.ui.checkBox_3:
                self.function_queue.append(lambda: clean(yandex_cache_path))
            elif self.sender() == self.ui.checkBox_5:
                self.function_queue.append(lambda: clean(temp_with_percent))

            self.count += 1
            self.ui.label_2.setText(f"{self.count}")
        
        elif status == Qt.CheckState.Unchecked and self.count > 0:
            # Убираем функцию из очереди, если чекбокс снят
            if self.sender() == self.ui.checkBox_2:
                self.function_queue.remove(clean)
            elif self.sender() == self.ui.checkBox_3:
                self.function_queue.remove(disable_edge)
            elif self.sender() == self.ui.checkBox_4:
                self.function_queue.remove(disable_cortana)
            elif self.sender() == self.ui.checkBox_5:
                self.function_queue.remove(lambda: clean(temp_with_percent))
            elif self.sender() == self.ui.checkBox_6:
                self.function_queue.remove(disable_windows_updates)
            elif self.sender() == self.ui.checkBox_7:
                self.function_queue.remove(disable_xbox_game_bar)
            elif self.sender() == self.ui.checkBox_8:
                self.function_queue.remove(restore_win10_context_menu)
            # Обновляем отображение количества выбранных функций
            self.count -= 1
            self.ui.label_2.setText(f"{self.count}")

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
    @Slot()
    def execute_functions(self):
        # Выполняем все функции из очереди
        for func in self.function_queue:
            try:
                func()
            except Exception as e:
                print(f"Ошибка при выполнении {func.__name__}: {e}")
        
        # Очищаем очередь после выполнения
        self.function_queue.clear()
        self.count = 0  # Сбрасываем счетчик
        self.ui.label_2.setText(f"Число выбранных вами функций: {self.count}")
        print("Все функции выполнены!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())
