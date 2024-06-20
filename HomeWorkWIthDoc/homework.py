import csv
import json
from math import ceil
from files import json_file
from files import csv_file
from csv import DictReader

result_file = "results.json"
books = []
with open(csv_file, 'r', newline='') as file_csv:
    reader = DictReader(file_csv)
    for row in reader:
        books.append(row)

with open(json_file, 'r', encoding='utf-8') as file_json:
    users = json.load(file_json)

num_books = len(books)
num_users = len(users)
books_per_user = ceil(num_books / num_users)

result = []
for user in users:
    user_data = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": []
    }
    result.append(user_data)


for i, book in enumerate(books):
    user_index = i % num_users
    result[user_index]["books"].append(book)
    # print(result[user_index]["books"])

with open(result_file,'w') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)
