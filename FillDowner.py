import csv
import tkFileDialog

				
with open('121 Computers in All Macs.csv', 'r') as f, open('results.csv', 'w') as results:
    reader = csv.reader(f)
    writer = csv.writer(results)

    for row in reader:
    	process_rows(row)

def process_rows(row):
	global a
	global b 
	
	if row[0] == "":
		row[0] = a
	else:
		a = row[0]
		
	if row[1] == "":
		row[1] = b
	else:
		b = row[1]
		
	writer.writerow(row)
	print row
    	
#    print f
#     print
#     print count

# def get_columns():
# 	empty_columns = list(raw_input("Which columns need to be filled? "))
# 	empty_columns = map(int, empty_columns)
# 	print empty_columns
    

# get_columns()

    # 14696 rows total
    # 11839 blanks