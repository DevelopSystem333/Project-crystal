from cleaning.temp import clean, cleanPapkaVPapke

def cleanMenu():
    b = input('Выберите пункт:\n1. Очистка папки temp\n2. Очистка папки prefetch\n3. Очистка кэша обновлений Windows\n4. Все пункты\n')
    temp_default = "C:/Windows/Temp"
    prefetch = "C:/Windows/Prefetch"
    cacheUpdate = "C:/Windows/SoftwareDistribution/Download"
    if b == '1':
        clean(temp_default)
        cleanPapkaVPapke(temp_default)
    if b == '2':
        clean(prefetch)
    if b == '3':
        clean(cacheUpdate)
        cleanPapkaVPapke(cacheUpdate)
    else:
        pass