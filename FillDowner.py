import sys
import csv
import Tkinter as tk
import tkFileDialog
import tkMessageBox

# Dialogs to select the files we're working with
def get_original_file():
    original_filename = ""
    
    root = tk.Tk()
    root.withdraw()
    original_filename = tkFileDialog.askopenfilename(defaultextension = ".csv")
    if original_filename == "":
        sys.exit("No file selected")
    elif original_filename.lower().endswith(".csv"):
        return original_filename
    else:
        tkMessageBox.showerror("Error!", "You must select a CSV file.", icon = "error")
        get_original_file()

def get_results_file():
	results_filename = ""

	root = tk.Tk()
	root.withdraw()
	results_filename = tkFileDialog.asksaveasfilename(defaultextension = ".csv")
	if results_filename == "":
		if tkMessageBox.askyesno("Cancel?", "Are you sure you want to cancel processing this file?"):
			sys.exit("File save cancelled")
		else:
			get_results_file()
	else:
		return results_filename

# The process to "fill down" the blank fields
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
 
# Do it!
originFile = get_original_file()
resultFile = get_results_file()

# Open the files and process them			
with open(originFile, 'r') as f, open(resultFile, 'w') as results:
    reader = csv.reader(f)
    writer = csv.writer(results)
 
    for row in reader:
    	process_rows(row)
      	
# def get_columns():
# 	empty_columns = list(raw_input("Which columns need to be filled? "))
# 	empty_columns = map(int, empty_columns)
# 	print empty_columns
#       
#   
# get_columns()
