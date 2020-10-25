import PyPDF2
import datetime
import os

PROJECT_DIR=os.path.abspath('.')
OUTPUT_FILE_URL = os.path.join(PROJECT_DIR,'static\merger\output')

def merge_pdfs(list_of_pdfs, output_name):

    pdfMergeHelper = PyPDF2.PdfFileMerger() 
      
    # merging pdf one by one 
    for pdf in list_of_pdfs:
        pdfMergeHelper.append(pdf)

    # Converted pdf file name
    PATH_TO_PDF = os.path.join(OUTPUT_FILE_URL, output_name)
          
    # Producing output file 
    pdfMergeHelper.write(PATH_TO_PDF)
    pdfMergeHelper.close()
        