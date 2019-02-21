import functions


def recursion_shit(path_list):

    for i in range(0, len(path_list["dir"])):
        path_list["dir"].append(functions.list_path_content(path_list["dir"][i]))

    return path_list

pat = "C:\ABB_repos\PanelTestAutomation\TestCases\AutomaticTests\ACX580"

aktualna_sciezka = functions.get_current_path(True)
zawartosc_slownik = functions.list_path_content(pat)
lista_h = recursion_shit(zawartosc_slownik)

print(lista_h)
