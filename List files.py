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
    current_path = get_current_path(False)
    dir_list = list_current_path_files_and_directories(current_path, False)

    for i in range(0, len(dir_list)):
        dir_path = os.path.join(current_path, dir_list[i])
        dir_path_list.append(dir_path)
    return dir_path_list


def split_list_into_directories_and_files(patch_list):
    directories = []
    files = []

    for patch_no in range (0, len(patch_list)):
        if os.path.isdir(patch_list[patch_no]):
            directories.append(patch_list[patch_no])
        else:
            files.append(patch_list[patch_no])

    split_patches = {
        "dir": directories,
        "fil": files
    }

    return split_patches


ona = create_current_directory_path_list()
eyn = split_list_into_directories_and_files(ona)
print(eyn["fil"])
