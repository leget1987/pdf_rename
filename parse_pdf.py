from os import listdir, rename, getcwd
import sys
import json

cur_dir = getcwd()

in_dir = sys.argv[1] 
if sys.argv[1][0] != '/': 
    in_dir = cur_dir + "/" + sys.argv[1]
result_json = []

for doc in listdir(in_dir):
    if doc[-3:] == 'pdf':
        temp_name = doc[:-4].split('_')
        result_json.append({doc: {"attributes": temp_name[:]}})

        # можно было бы  задействовать регулярные выражения
        if 'cj' in doc.lower() or 'jc' in doc.lower():
            continue
        temp_name[0], temp_name[-1] = temp_name[-1], temp_name[0]

        temp_name_rename = '_'.join(temp_name) + ".pdf"
        result_json.append({temp_name_rename: {"attributes": temp_name, "after": 1}})


        rename(f'./pdf/{doc}', f'./pdf/{temp_name_rename}')

with open ('ressult.json', 'w') as f:
    json.dump(result_json, f)
