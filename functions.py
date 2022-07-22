import json

#-----------------------------------------------------------------------------------------------------
#ova funkcija get_json_data nam omogucava da svaki put preuzmemo podatke iz
#dictionary_names JSON datoteke i dodijelimo ga u neku (novu) lokalnu varijablu.
def get_json_data():
    with open("dictionary_names.json", "r") as dictionary_data:
        dict_obj = json.loads(dictionary_data.read())

    return dict_obj



def write_to_json():
    pass



#-----------------------------------------------------------------------------------------------------
def json_proba(key, value):

    with open("dictionary_names.json", "r") as sadrzaj:
        dict_obj = json.loads(sadrzaj.read())

    print(dict_obj)

    if key in dict_obj and value in dict_obj[key]:

        print("Vec postoji odgovor {0}!".format(value))

#ovdje dodaje novu vrijednost koju zadamo u "dict_obj" ---> to je ustvari ocitan sadrzaj iz JSON
#datoteke!

    elif key in dict_obj:
        dict_obj[key].append(value)

        with open("dictionary_names.json", "w") as sadrzaj_a:
            sadrzaj_a.write(json.dumps(dict_obj))
            print("Uspjesno ste dodali novi odgovor - ''{0}'', na postojecu reakciju ''{1}''!".format(value, key))

    else:
        # As key is not in dict, so add key-value pair
        dict_obj[key] = value

        with open("dictionary_names.json", "w") as sadrzaj_a:
            sadrzaj_a.write(json.dumps(dict_obj))

        print("Dodan je novi key-value par.")
        print("Novi key u dictionaryju je - {0}, a value je - {1}".format(key, value))



#ovdje cu napraviti funkciju koja uzima random odabir iz dictionary_names datoteke i
#vraca onda neki odgovor ovisno o mojoj "input" recenici --
    #npr. ja napisem "Kako se osjecas?"
        #odgovor bi na to bio od programa: "Sretno/Tuzno/..."

#------------------------------------------------------------------------------------------------------
def reakcija():
    pass