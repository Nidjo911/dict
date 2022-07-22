# pocetni dio koda

import json
import random
from prettytable import PrettyTable
from functions import json_proba, get_json_data

#---------------------------------------------------------------------------
#funkcija json_proba dodaje u JSON "dictionary_names" novu reakciju!

while True:

        #dio koda koji izabire u koju ce se kategoriju dodati novi "response"

        #enumerirani dict napraviti iz "dictionary_names":
        dict_obj = get_json_data()

        #with open("dictionary_names.json", "r") as dictionary_data:
        #    dict_obj = json.loads(dictionary_data.read())

        for i, j in dict_obj.items():
            print("{0} - {1}".format(i, j))

        display_dict = {}

        for index, key in enumerate(dict_obj):
            display_dict[str(index + 1)] = key

        for key, value in display_dict.items():
            print("{0} - {1}".format(key, value))

        print("---> Odaberite '0' za izlaz iz programa! <---")

        izbor = input("U koju kategoriju zelite dodati novu rijec? Napisite ovdje: ")

        if izbor == "0":
            break

        elif izbor in display_dict:

            izabrana_reakcija = display_dict[izbor]
            print("Izabrana reakcija je: {0}".format(izabrana_reakcija))

            while True:

                print("---------------------------------------------------------------------------------")
                print("---> Odaberite '0' za izlaz iz programa! <---\n\t")
                nova_rijec = input("Napisite NOVU rijec koju zelite dodati u izabranu reakciju ({0}):\n".format(izabrana_reakcija))

                if nova_rijec == "0":
                    break

                else:
                    for i, j in dict_obj.items():

                        if nova_rijec in dict_obj[display_dict[izbor]]:
                            print("Ta reakcija vec postoji, molim odaberite neku drugu!")
                            break

                        else:
                            dict_obj[izabrana_reakcija].append(nova_rijec)

                            with open("dictionary_names.json", "w") as sadrzaj_a:
                               sadrzaj_a.write(json.dumps(dict_obj))

                            print("Cestitam! Tvoj dict. sada izgleda ovako: \n")
                            print(get_json_data())

                            break