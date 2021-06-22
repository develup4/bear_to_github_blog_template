import os

if __name__ == "__main__":
    with os.scandir() as entries:
        for entry in entries:
            if entry.name.split('.')[1] != 'py':
                os.remove(entry.name)