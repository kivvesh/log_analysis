import os


def is_dir_or_file(path):
    if not os.path.exists(path):
        raise Exception('Путь некорректный')
    if os.path.isdir(path):
        return True
    return False

def get_all_files_from_dir(dir):
    list_files = os.listdir(dir)
    currect_list_files = []
    for file in list_files:
        if os.path.isdir(os.path.join(dir,file)):
            currect_list_files += get_all_files_from_dir(os.path.join(dir,file))
        else:
            currect_list_files.append(os.path.join(dir,file))
    if len(currect_list_files) == 0:
        raise Exception('В директории отсутствуют файлы')
    return currect_list_files