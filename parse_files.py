import json
import csv

def parse_files(json_filename, csv_filename):
    
    with open(f"{json_filename}", "r") as json_file:
        users = json.loads(json_file.read())

    with open(f'{csv_filename}', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        iter_user = iter(users) # iterator for each user from the list
        for row in reader:
            try:
                user = next(iter_user)  # return each user in order
            except StopIteration:
                iter_user = iter(users)
                user = next(iter_user)

            if "books" not in user.keys():
                user["books"] = []
            else:
                user["books"].append({
                    "title": row["Title"],
                    "author": row["Author"],
                    "pages": row["Pages"],
                    "genre": row["Genre"]
                })

    result_data = []

    for user in users:
        result_data.append({
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": user["books"]
        })
    return result_data
  