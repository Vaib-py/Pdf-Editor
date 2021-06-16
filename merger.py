import PyPDF2 
import sys 

# Inputing Pdfs

input = sys.argv[1:]

# Making function for the same

def Pdf_merger (pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('merged.pdf')
Pdf_merger(input)    