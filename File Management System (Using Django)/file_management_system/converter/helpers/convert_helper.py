import sys
import subprocess
import re
import os
from threading import Thread

PROJECT_DIR=os.path.abspath('.')
OUTPUT_FILE_URL = os.path.join(PROJECT_DIR,'static\converter\output')

def convert_to(folder, source, output_file_name, timeout=None):
    args = [libreoffice_exec(), '--headless', '--convert-to', 'pdf', '--outdir', folder, source]
    OUTPUT_FILE_PATH = os.path.join(folder, output_file_name)
    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    print(process)
    filename = re.search('-> (.*?) using filter', process.stdout.decode())
    print(filename)
    os.rename(filename.group(1), OUTPUT_FILE_PATH)

    if filename is None:
        raise LibreOfficeError(process.stdout.decode())
    else:
        return OUTPUT_FILE_PATH


def libreoffice_exec():
    #support for windows platforms
    if sys.platform == 'win32':
        return "C:\Program Files\LibreOffice\program\soffice"
    return 'libreoffice'


class LibreOfficeError(Exception):
    def __init__(self, output):
        self.output = output

def start_converting(source, output_file_name):
    thread = Thread(target = convert_to,args=(OUTPUT_FILE_URL, source, output_file_name,))
    thread.start()
