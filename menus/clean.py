from cleaning.temp import clean

def cleanMenu():
    b = input('Выберите пункт:\n1. Очистка папки temp\n2. Очистка папки prefetch\n3. Все пункты\n')
    temp_default = "C:/Windows/Temp"
    prefetch = "C:/Windows/Prefetch"
    if b == '1':
        clean(temp_default)
    if b == '2':
        clean(prefetch)
    else:
        pass