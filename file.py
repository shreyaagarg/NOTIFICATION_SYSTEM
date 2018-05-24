# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('syll.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

list = []

# creating a page object
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    data = pageObj.extractText()
    try:
        data1 = data.split('\n')
        index1 = data1.index('Course Code')
        index2 = data1 .index('Course Name     ')
        index3 = data1.index('Credits')
        string = (data1[index1+4] , data1[index2+4])
        with open("CourseInfo.txt", 'a') as file:
            file.write("("+ "\'" + data1[index1+4]  + "\'" +  ',' + "\'" +  data1[index2+4]+ "\'" +  ',' + "\'" +  data1[index3+4]+ "\'" ")" + ",\n")
    except Exception as e:
        print(e)
        pass


# closing the pdf file object
pdfFileObj.close()
file.close()