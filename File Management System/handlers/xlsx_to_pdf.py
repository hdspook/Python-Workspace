def generate(file_name):
    import os
    import datetime
    import win32com.client
    from pywintypes import com_error


    # Path to original excel file
    WB_PATH = file_name
    # PDF path when saving
    BASE_NAME = os.path.basename(WB_PATH)
    TIME_STAMP = str(round(datetime.datetime.now().timestamp())) 
    PATH_TO_PDF = WB_PATH[0:WB_PATH.find(BASE_NAME)] + "converted_" + BASE_NAME[0:-5] + "_" + TIME_STAMP + ".pdf"


    excel = win32com.client.Dispatch("Excel.Application")

    excel.Visible = False

    # Open
    wb = excel.Workbooks.Open(WB_PATH)

    try:
        print('Start conversion to PDF')
        # Specify the sheet you want to save by index. 1 is the first (leftmost) sheet.
        ws_index_list = [1]
        wb.WorkSheets(ws_index_list).Select()

        # Save
        wb.ActiveSheet.ExportAsFixedFormat(0, PATH_TO_PDF)
    except com_error as e:
        print('failed.')
    else:
        print('Succeeded.')
    finally:
        wb.Close()
        excel.Quit()