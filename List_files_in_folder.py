import functions


def list_directories_one(path_list):
    list = path_list
    for i in range(0, len(path_list[0])):
        list = list + (functions.list_path_content(path_list[0][i]))
        print(list)

    return list

#pat = "C:\ABB_repos\PanelTestAutomation\TestCases\AutomaticTests\ACX580"
#pat = functions.get_current_path(False)

#zawartosc_slownik = functions.list_path_content(pat)
#print(len(zawartosc_slownik[0]))

#lista_h = list_directories_one(zawartosc_slownik)
#print(lista_h)


pat = functions.get_current_path(False)
lis = functions.list_path_content(pat)
#print(lis)


def funcc(path_lol):
    for i in range (0, len(path_lol)):
        print("########################### "+ path_lol[i])
        ten = functions.list_path_content(path_lol[i])
        print(ten[0])


funcc(lis[0])

