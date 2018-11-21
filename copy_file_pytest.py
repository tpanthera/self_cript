import xlrd

# File name is present in excel sheet
# variables : File_name.py , method_name = File_name ,  " comment section : { "main_service_name" ," service_details", " File_name" , }
#   test_load = " sheet_input_data"  ,api_url = "sheet_APi_url" , api_url_caps_on"
#
#
# read excel and extract the file name and increment

loc = "D:\python codes\script_ofyc\ip_sheet.xlsx"

reader = xlrd.open_workbook(loc)
sheet = reader.sheet_by_index(0)
row_max_value = [1,2,3]
col_max_value = [0,1,2,3,4,5]
'''
for i in row_max_value:
    for j in col_max_value:
        print(sheet.cell_value(i,j))
'''

for i in row_max_value:
    with open("D:\python codes\script_ofyc\ip.py") as f_ip:
            with open("D:\python codes\script_ofyc\\" + sheet.cell_value(i,1),"w") as f_op:
                for line in f_ip:
                    line = line.replace( 'Main_service_name', sheet.cell_value(i,1))
                    line - line.replace()
                    f_op.write(line)
