import os
import shutil

def clean(dir):
    for item in os.listdir(dir):
        item_path = os.path.join(dir, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        except Exception as e:
            print(f'Ошибка при удалении {item_path} | {e}')