import functions


def funkc2(path, i):
    if i == len(path):
        print(len(path))
        return path

    path += functions.list_path_content(path[i])
    i += 1
    return funkc2(path, i)

pat = [functions.get_current_path(False)]
#pat = ["C:\ABB_repos\PanelTestAutomation\TestCases\AutomaticTests\ACX580"]
oto = funkc2(pat, 0)
print(oto)