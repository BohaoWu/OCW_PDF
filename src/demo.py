import PyPDF2 as pyPDF
import os

course_name = '计算机网络'

merger = pyPDF.PdfMerger()
path = os.getcwd().replace('\\src', '')
resource_document_path = '../resource'
files = os.listdir('..\\resource\\' + course_name)
outputPath = '..\\doc\\' + course_name +".pdf"
print(files)

for pdf in files:
    file_path = path+'\\resource\\'+course_name+'\\'+pdf
    print(pdf, file_path)
    # input = open(file_path, encoding='locale', errors='ignore')
    # pdf_file = pyPDF.PdfReader(file_path)
    # input = open(path+'\\files\\'+pdf, encoding='locale', errors='ignore')
    # input = open(path+'\\files\\'+pdf,'rb')
    merger.append(fileobj=file_path)

# outputStream = open(outputPath,)
merger.write('../doc/'+outputPath)
merger.close()
# outputStream.close()