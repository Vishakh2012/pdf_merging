#a program that merges all the pdfs in a folder in ascii order of naming
from pathlib import Path # importing the Path class from the pathlib module
from PyPDF2 import PdfFileMerger

reports_dir = Path(input('enter the file path:'))
"""
   this program searches for all the pdf files in a folder, then merges all of them into a single pdf, which gets saves in the current working directory. 
"""

expense_reports = list(reports_dir.glob("*.pdf"))#creating a list that contains all the pdfs in the path object
expense_reports.sort()#sorting the list to get an ordered list

merger = PdfFileMerger()#creating the pdf file merger object
for path in expense_reports:
    merger.append(str(path))#append is used to add the pdf to the end of the object

    #note that the path is converted into string before passing it into the method

with Path("new.pdf").open(mode="wb") as output:
    merger.write(output)#same as when using the pdf writer the object
  