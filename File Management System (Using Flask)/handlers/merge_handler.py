import PyPDF2
import datetime
import os

TIME_STAMP = str(round(datetime.datetime.now().timestamp()))

def merge_pdfs(list_of_pdfs):

    pdfMergeHelper = PyPDF2.PdfFileMerger() 
      
    # merging pdf one by one 
    for pdf in list_of_pdfs:
        pdfMergeHelper.append(pdf)

    # Path to original PDFS
    WB_PATH = list_of_pdfs[0]
    # PDF path when saving
    BASE_NAME = os.path.basename(WB_PATH)
    # Converted pdf file name
    PATH_TO_PDF = WB_PATH[0:WB_PATH.find(BASE_NAME)] + "merged_" + BASE_NAME[0:-4] + "_" + TIME_STAMP + ".pdf"
          
    # Producing output file 
    pdfMergeHelper.write(PATH_TO_PDF)
    pdfMergeHelper.close()
        