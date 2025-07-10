from optimization.xboxGB import disable_xbox_game_bar
from optimization.cortana import disable_cortana
from optimization.browser import disable_edge
def optimizationMenu():
    c = input('Выберите пункт:\n1. Отключение Xbox Game Bar\n2. Отключение Cortana\n3. Отключение Microsoft Edge\n4. Отключение обновлений windows\n')
    if c == '1':
        disable_xbox_game_bar()
    if c == '2':
        disable_cortana()
    if c == '3':
        disable_edge()
    else:
        pass