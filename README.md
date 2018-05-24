# FillDowner
Fill in empty CSV fields from previous record (like Excel's "Fill Down" command).

### Why?
I was working with a report from JSS that my superiors wanted sorted differently. But, the report had some blanks setup for easier viewing of the data, like this:

First Field  | Second Field
------------- | -------------
Rob  | Item 1
[blank]  | Item 2
John  | Item 1
[blank]  | Item 2
  
I could open it with Excel and "fill down" for each blank section; but, I had 14k rows. And, I have no interest in learning VBScript to create an Excel macro.

So, this is a good learning opportunity for me with Python.

###What?
This script examines each row, checking the requested fields (currently 1 and 2 since that is what I initially needed) for blanks. If it finds a blank, it changes it to that field's entry from the previous non-blank record.

###Future?
As I'm learning Python, I want to:

- add GUI dialogs to select the original file and name the results file
- add a field selector to select which fields you want to "fill"
- add some logic to recommend which fields to "fill"
