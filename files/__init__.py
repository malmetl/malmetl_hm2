import os.path

files_dir = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(files_dir, filename)


json_file = get_path('users.json')
csv_file = get_path('books.csv')
