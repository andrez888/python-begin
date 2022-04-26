def added_people_group(present_list,future_list = None):
    if  future_list is None:
        future_list = []
    lista = present_list.split(',')
    for list in lista:
        future_list.append(list)
    return future_list

x ="marek,tomek,adrian"
stara_lista = added_people_group(x)
print(stara_lista)
b= "andrzej,agata"
nowa_lista = added_people_group(b,stara_lista)
print(nowa_lista)