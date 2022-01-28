import json

from download_files import download_save_files
from parse_files import parse_files

json_filename = 'users.json'
csv_filename = 'books.csv'

download_save_files(json_filename, csv_filename) # they're already saved so this step might be skipped

result = parse_files(json_filename, csv_filename)

with open("result.json", "w") as f:
    s = json.dumps(result, indent=4)
    f.write(s)