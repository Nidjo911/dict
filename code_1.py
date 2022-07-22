import json
import random
from prettytable import PrettyTable
from functions import get_json_data

dict_obj = get_json_data()

for i, j in dict_obj.items():
    print("{0} - {1}".format(i, j))