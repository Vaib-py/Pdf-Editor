import PyPDF2

temp = PyPDF2.PdfFileReader(open('merged.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range (temp.getNumPages()):
    page = temp.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    
    with open ('watermarker.pdf', 'wb') as file :
        output.write(file)




