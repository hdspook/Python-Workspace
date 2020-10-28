import PyPDF2
import datetime
import os

#get the output directory
PROJECT_DIR=os.path.abspath('.')
OUTPUT_FILE_URL = os.path.join(PROJECT_DIR,'static\merger\output')

#get the timestamp to name the file
TIME_STAMP = str(round(datetime.datetime.now().timestamp()))

def merge_pdfs(list_of_pdfs):

    pdfMergeHelper = PyPDF2.PdfFileMerger()
    file_info = []
    
    try:
            
        # Path to original PDFS
        WB_PATH = list_of_pdfs[0]
        # PDF path when saving
        BASE_NAME = os.path.basename(WB_PATH)
        # Converted pdf file name
        OUTPUT_FILE_NAME = "merged_" + BASE_NAME[0:-4] + "_" + TIME_STAMP + ".pdf"
        # Converted pdf file name
        PATH_TO_PDF = os.path.join(OUTPUT_FILE_URL, OUTPUT_FILE_NAME)

        # merging pdf one by one 
        for pdf in list_of_pdfs:
            pdfMergeHelper.append(pdf)

        # Producing output file 
        pdfMergeHelper.write(PATH_TO_PDF)

        file_info.append(OUTPUT_FILE_NAME)
        file_info.append(PATH_TO_PDF)
        file_info.append('success')

        return file_info

    except:
        file_info.append("NA")
        file_info.append("NA")
        file_info.append('failed')

        return file_info

    finally:
        pdfMergeHelper.close()
        