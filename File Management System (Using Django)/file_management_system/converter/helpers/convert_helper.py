import sys
import subprocess
import re
import os
import datetime
from threading import Thread

PROJECT_DIR=os.path.abspath('.')
OUTPUT_FILE_URL = os.path.join(PROJECT_DIR,'static\converter\output')

TIME_STAMP = str(round(datetime.datetime.now().timestamp()))

def convert_to(folder, source, timeout=None):
    file_info = []

    args = [libreoffice_exec(), '--headless', '--convert-to', 'pdf', '--outdir', folder, source]

    # PDF path when saving
    BASE_NAME = os.path.basename(source)
    # Converted pdf file name
    PATH_TO_PDF ="converted_" + BASE_NAME[0:-5] + "_" + TIME_STAMP + ".pdf"
    OUTPUT_FILE_PATH = os.path.join(folder, PATH_TO_PDF)

    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    filename = re.search('-> (.*?) using filter', process.stdout.decode())

    os.rename(filename.group(1), OUTPUT_FILE_PATH)

    file_info.append(os.path.basename(OUTPUT_FILE_PATH))
    file_info.append(OUTPUT_FILE_PATH)
    file_info.append('success')

    if filename is None:
        print(LibreOfficeError(process.stdout.decode()))
        file_info = ["NA", "NA", "Failed"]
    return file_info


def libreoffice_exec():
    #support for windows platforms
    if sys.platform == 'win32':
        return "C:\Program Files\LibreOffice\program\soffice"
    return 'libreoffice'


class LibreOfficeError(Exception):
    def __init__(self, output):
        self.output = output

def start_converting(source):
    return(convert_to(OUTPUT_FILE_URL, source))
    # thread = Thread(target = convert_to,args=(OUTPUT_FILE_URL, source,))
    # thread.start()
