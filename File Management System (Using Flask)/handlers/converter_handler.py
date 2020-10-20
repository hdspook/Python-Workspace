from docx2pdf import convert
from threading import Thread
from .xlsx_to_pdf import generate
import pythoncom
import pandas as pd
import csv
import os
import datetime

TIME_STAMP = str(round(datetime.datetime.now().timestamp()))


def convert_data_xlsx(file_name):
    with open('details.csv','a') as details_file:
        file_writer = csv.writer(details_file, delimiter = ',')

        with open(file_name,'r') as txt_file:
            for line in txt_file:
                single_detail = line.split(",")
                file_writer.writerow(single_detail)

    # Reading the csv file 
    pd_reader = pd.read_csv('details.csv') 
  
    # saving xlsx file 
    workbook = pd.ExcelWriter('patients_details.xlsx') 
    pd_reader.to_excel(workbook, index = False) 
    workbook.save()

def docx_to_pdf(file_name):
    
    # Path to original DOCX file
    WB_PATH = file_name
    # PDF path when saving
    BASE_NAME = os.path.basename(WB_PATH)
    # Converted pdf file name
    PATH_TO_PDF = WB_PATH[0:WB_PATH.find(BASE_NAME)] + "converted_" + BASE_NAME[0:-5] + "_" + TIME_STAMP + ".pdf"
    #COM initializing to access WORD Application
    pythoncom.CoInitialize()
    convert(file_name, PATH_TO_PDF)


def xlsx_to_pdf(file_name):
    #COM initializing to access WORD Application
    pythoncom.CoInitialize()
    generate(file_name)
