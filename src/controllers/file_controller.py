import shutil
import os
import re
from configs import Application


def check_folder_exist(path_folder):
    return os.path.exists(path_folder)


def check_file_exist(path_file):
    return os.path.isfile(path_file)


def create_folder_by_path(path_folder, mode=None):
    if not check_folder_exist(path_folder):
        os.makedirs(path_folder, exist_ok=True)
        if mode:
            os.chmod(path_folder, mode)


def get_path_file(path=None, file_name=None, is_path_df=True, is_create=True):
    if is_path_df:
        if path:
            path = Application.WORKING_DIR + '/' + path
        if not path:
            path = Application.WORKING_DIR
        path = path.replace('//', '/')
        if is_create:
            create_folder_by_path(path)
        return os.path.join(path, file_name)
    else:
        path = path.replace('//', '/')
        if os.path.exists(path):
            return os.path.join(path, file_name)
        if is_create:
            create_folder_by_path(path)
        return os.path.join(path, file_name)
