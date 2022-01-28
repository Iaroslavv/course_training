import requests

books_response = requests.get('https://raw.githubusercontent.com/konflic/front_example/master/data/books.csv').content
users_response = requests.get('https://raw.githubusercontent.com/konflic/front_example/master/data/users.json').content

def download_save_files(json_filename, csv_filename):
    #use it to download and save csv file
    with open(f'{csv_filename}', 'wb') as csvfile:
        csvfile.write(books_response)

    #use it to download and save json file
    with open(f'{json_filename}', 'wb') as jsonfile:
        jsonfile.write(users_response)