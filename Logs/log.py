import datetime
from desing import Ui_MainWindow

# Предположим, main_window — это глобальная переменная,
# содержащая ссылку на главное окно вашего приложения
main_window = None

def set_main_window(window):
    global main_window
    main_window = window

def clog(text):
    if main_window is not None and hasattr(main_window, 'ui'):
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        main_window.ui.textEdit.insertPlainText(f'[{current_time}] {text}\n')