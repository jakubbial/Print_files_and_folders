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


def create_directories_path(current_path, dir_list):
    dir_path_list = []
    for i in range(0, len(dir_list)):
        dir_path = os.path.join(current_path, dir_list[i])
        dir_path_list.append(dir_path)
    return dir_path_list


curr_path = get_current_path(True)
fil_dir_list = list_current_path_files_and_directories(curr_path, True)

ona = create_directories_path(curr_path, fil_dir_list)
print(ona)
