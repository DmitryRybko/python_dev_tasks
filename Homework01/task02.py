"""
2. Дополнить следующую функцию недостающим кодом:
"""
import os


def print_directory_contents(sPath):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """

    base_folder = sPath
    dir_contents = os.listdir(base_folder)
    for child in dir_contents:
        path = os.path.join(base_folder, child)
        if os.path.isdir(path):
            print("DIR: " + "\t" + path)
            print_directory_contents(path)
        else:
            print("file: " + "\t" + path)


folder_input = "C:\python_course\python_dev_tasks"
print_directory_contents(folder_input)


"""
Result:
DIR: 	C:\python_course\python_dev_tasks\.git
file: 	C:\python_course\python_dev_tasks\.git\COMMIT_EDITMSG
file: 	C:\python_course\python_dev_tasks\.git\config
file: 	C:\python_course\python_dev_tasks\.git\description
file: 	C:\python_course\python_dev_tasks\.git\FETCH_HEAD
file: 	C:\python_course\python_dev_tasks\.git\HEAD
DIR: 	C:\python_course\python_dev_tasks\.git\hooks
file: 	C:\python_course\python_dev_tasks\.git\hooks\applypatch-msg.sample
file: 	C:\python_course\python_dev_tasks\.git\hooks\commit-msg.sample
file: 	C:\python_course\python_dev_tasks\.git\hooks\fsmonitor-watchman.sample
file: 	C:\python_course\python_dev_tasks\.git\hooks\post-update.sample
file: 	C:\python_course\python_dev_tasks\.git\hooks\pre-applypatch.sample
file: 	C:\python_course\python_dev_tasks\.git\hooks\pre-commit.sample
и т.д.
"""