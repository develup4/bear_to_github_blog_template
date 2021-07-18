import os
import shutil

if __name__ == "__main__":
    with os.scandir() as entries:
        for entry in entries:
            if entry.is_file() == False:
                shutil.rmtree(entry)
            elif entry.name.split('.')[1] != 'py':
                os.remove(entry.name)