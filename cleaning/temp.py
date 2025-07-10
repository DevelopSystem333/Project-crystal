import os

def clean(dir):
    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)
        try:
            os.remove(file_path)
        except Exception as e:
            print(f'Ошибка при удалении файла: {file_path} | {e}')