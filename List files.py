import os


# Returns working directory path

def get_current_path(do_print):
    current_path = os.getcwd()
    if do_print:
        print(current_path)
    return current_path


# Function that changing current working directory

def change_directory(destination_path):
    os.chdir(destination_path)


# Function return dictionary ('dir', 'fil') that contain content of given path

def list_path_content(path_to_list):
    directories = []
    files = []
    dir_list = os.listdir(path_to_list)

    for i in range(0, len(dir_list)):
        dir_path = os.path.join(path_to_list, dir_list[i])

        if os.path.isdir(dir_path):
            directories.append(dir_path)
        else:
            files.append(dir_path)

    split_patches = {
        "dir": directories,
        "fil": files
    }
    return split_patches


aktualna_sciezka = get_current_path(False)
zawartosc_slownik = list_path_content(aktualna_sciezka)
print(zawartosc_slownik["dir"])
print(zawartosc_slownik["fil"])
