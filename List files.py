import os


def list_current_path_files_and_directories(path, do_print):
    directory_list = os.listdir(path)
    if do_print:
        print(directory_list)
    return directory_list


def get_current_path(do_print):
    current_path = os.getcwd()
    if do_print:
        print(current_path)
    return current_path


def change_directory(destination_path):
    os.chdir(destination_path)


def create_current_directory_path_list():
    dir_path_list = []
    current_path = get_current_path(True)
    dir_list = list_current_path_files_and_directories(current_path, False)

    for i in range(0, len(dir_list)):
        dir_path = os.path.join(current_path, dir_list[i])
        dir_path_list.append(dir_path)
    return dir_path_list


def split_list_into_directories_and_files(patch_list):
    for patch_no in range (0, len(patch_list)):
        print(patch_list[patch_no])


ona = create_current_directory_path_list()
split_list_into_directories_and_files(ona)
