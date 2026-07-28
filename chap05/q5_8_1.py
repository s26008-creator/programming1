country_code ={
        'Iceland': {'code': '354', 'capital': 'Reykjavil'},
        'Ireland': {'code': '353', 'captial': 'Dublin'},
        'Azerbaidjan': {'code': '994', 'captial': 'Baku'}
        }

def getstr_keyval(x):
    if not isinstance(x, dict):
        return x

    my_str = ''
    for key, val in x.items():
        my_str += (' ' + str(key) + ' ' + getstr_keyval(val))
    return my_str

for key1, val1 in country_code.items():
    print(key1, getstr_keyval(val1))
