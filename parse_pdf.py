from os import listdir, rename, getcwd
import sys
import json

# cur_dir = getcwd()

# in_dir = sys.argv[1]
# if sys.argv[1][0] != '/':
#     in_dir = cur_dir + "/" + sys.argv[1]
# result_json = []

# for doc in listdir(in_dir):
#     if doc[-3:] == 'pdf':
#         temp_name = doc[:-4].split('_')
#         result_json.append({doc: {"attributes": temp_name[:]}})

#         # можно было бы  задействовать регулярные выражения
#         if 'cj' in doc.lower() or 'jc' in doc.lower():
#             continue
#         temp_name[0], temp_name[-1] = temp_name[-1], temp_name[0]

#         temp_name_rename = '_'.join(temp_name) + ".pdf"
#         result_json.append(
#             {temp_name_rename: {"attributes": temp_name, "after": 1}})

#         rename(f'{in_dir}/{doc}', f'{in_dir}/{temp_name_rename}')

# with open('ressult.json', 'w') as f:
#     json.dump(result_json, f)


class ParseArgs:

    def __init__(self, in_dir: str) -> None:
        self.in_dir = in_dir

    def init_data(self):
        cur_dir = getcwd()
        if self.in_dir[0] != '/':
            self.in_dir = cur_dir + "/" + self.in_dir
        return self.in_dir


class PdfParser:

    def __init__(self, in_dir: str) -> None:
        self.in_dir = in_dir
        self.result_json = []

    def run_parser(self):
        for doc in listdir(self.in_dir):
            if doc[-3:] == 'pdf':
                temp_name = doc[:-4].split('_')
                self.result_json.append({doc: {"attributes": temp_name[:]}})

                # можно было бы  задействовать регулярные выражения
                if 'cj' in doc.lower() or 'jc' in doc.lower():
                    continue
                temp_name[0], temp_name[-1] = temp_name[-1], temp_name[0]

                temp_name_rename = '_'.join(temp_name) + ".pdf"
                self.result_json.append(
                    {temp_name_rename: {"attributes": temp_name, "after": 1}})

                rename(f'{self.in_dir}/{doc}',
                       f'{self.in_dir}/{temp_name_rename}')
        return self.result_json


class SaveJSON:

    def __init__(self, result_json: list, save_path: str) -> None:
        self.result_json = result_json
        self.save_path = save_path

    def save_result(self) -> None:
        with open(self.save_path, 'w') as f:
            json.dump(self.result_json, f)


parse_arg = ParseArgs(sys.argv[1])
parse_dir = parse_arg.init_data()
pdf_parser = PdfParser(parse_dir)
result_json = pdf_parser.run_parser()
SaveJSON(result_json, 'result.json').save_result()
