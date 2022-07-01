#ova funkcija omogucava dodavanje novog  value unutar postojeceg
#key-a u dictu.

#preuzeto sa web stranice:
#https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/

def append_value(dict_obj, key, value):
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        if not isinstance(dict_obj[key], list):
            # If type is not list then make it list
            dict_obj[key] = [dict_obj[key]]
        # Append the value in list
        dict_obj[key].append(value)
    else:
        # As key is not in dict,
        # so, add key-value pair
        dict_obj[key] = value
# Dictionary of strings and ints
word_freq = {"Hello": 56,
             "at": 23,
             "test": 43,
             "this": 43}
append_value(word_freq, 'at', 21)
print(word_freq)