import xlsxwriter
from datetime import datetime

school_data = [['Computer Science', 235, 3.44, datetime(2015, 07, 23, 18, 00, 00)],
               ['Chemistry', 201, 3.26, datetime(2015, 07, 25, 9, 30, 00)],
               ['Forensics', 99, 3.8, datetime(2015, 07, 23, 9, 30, 00)],
               ['Astronomy', 115, 3.21, datetime(2015, 07, 19, 15, 30, 00)]]


def writeXLSX(data):
    workbook = xlsxwriter.Workbook('MyWorkbook.xlsx')
    main_sheet = workbook.add_worksheet('MySheet')

    date_format = workbook.add_format({'num_format': 'mm/dd/yy hh:mm:ss AM/PM'})
    length = str(len(data) + 1)
    main_sheet.add_table(('A1:D' + length), {'data': data,
                                             'columns': [{'header': 'Department'}, {'header': 'Students'},
                                                         {'header': 'Cumulative GPA'},
                                                         {'header': 'Final Date', 'format': date_format}]})
    workbook.close()


writeXLSX(school_data)