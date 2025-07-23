from optimization.xboxGB import disable_xbox_game_bar
from optimization.cortana import disable_cortana
from optimization.browser import disable_edge
from optimization.update import disable_windows_updates
from optimization.perfomance import performance_mode
def optimizationMenu():
    c = input('Выберите пункт:\n1. Отключение Xbox Game Bar\n2. Отключение Cortana\n3. Отключение Microsoft Edge\n4. Отключение обновлений windows\n5. Включить наилучшее быстродействие(отключение анимаций...)\n')
    if c == '1':
        disable_xbox_game_bar()
    if c == '2':
        disable_cortana()
    if c == '3':
        disable_edge()
    if c == '4':
        disable_windows_updates()
    if c == '5':
        performance_mode()
    else:
        pass