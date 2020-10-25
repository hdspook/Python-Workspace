import os

PROJECT_DIR=os.path.abspath(".")
INPUT_FILE_URL = os.path.join(PROJECT_DIR,"static\converter\input")

def file_url_list(data):
    expected = [os.path.join(INPUT_FILE_URL, x) for x in data.split(",")]
    return expected
