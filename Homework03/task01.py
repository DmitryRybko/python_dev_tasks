"""
1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
В функции необходимо реализовать поиск полного пути по имени файла,
а затем «выделение» из этого пути имени файла (без расширения)
"""

import os


def get_name_from_path(file_name_ext):
    file_name = file_name_ext
    current_dir = os.getcwd()
    full_path = os.path.join(current_dir, file_name)
    print(f'полный путь до файла: {full_path}')
    file_name_extracted = os.path.basename(full_path)
    file_name_wo_ext = os.path.splitext(file_name_extracted)[0]
    print(f'имя файла без расширения: {file_name_wo_ext}')
    return file_name


full_file_name = "task01.py"

get_name_from_path(full_file_name)
