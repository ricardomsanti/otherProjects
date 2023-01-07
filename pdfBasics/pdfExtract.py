import PyPDF2 as pdf 

#creating a pdf reader object from a given path


def create_file(path = None):
    
    with open(path, "rb") as pdf_FileObj:
        pdfReader = pdf.PdfFileReader(pdf_FileObj)        
        print(pdfReader.numPages)


create_file("flask-palletsprojects-com-en-1.1.x.pdf")        



