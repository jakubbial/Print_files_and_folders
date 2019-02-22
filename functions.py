import os


# Returns working directory path

def get_current_path(do_print):
    current_path = os.getcwd()
    if do_print:
        print(current_path)
    return current_path


# Function return dictionary ('dir', 'fil') that contain content of given path

def list_path_content(path_to_list):
    directories = []
    files = []
    directory_content_list = os.listdir(path_to_list)

    for i in range(0, len(directory_content_list)):
        dir_path = os.path.join(path_to_list, directory_content_list[i])

        if os.path.isdir(dir_path):
            directories.append(dir_path)
        else:
            files.append(dir_path)

    split_patches = directories

    return split_patches


def list_content_of_all_path_folders(path, i):
    if i == len(path):
        return path

    path += list_path_content(path[i])
    i += 1
    return list_content_of_all_path_folders(path, i)


# pat = [get_current_path(False)]
pat = ["C:\ABB_repos\PanelTestAutomation\TestCases\AutomaticTests\ACX580"]


oto = list_content_of_all_path_folders(pat, 0)
print(oto)
