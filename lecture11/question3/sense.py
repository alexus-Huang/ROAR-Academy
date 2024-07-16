import PyPDF2
import os

path = os.path.dirname(os.path.abspath(__file__))
f_p = os.path.join(path, "Sense-and-Sensibility-by-Jane-Austen.pdf")
file_handle = open(f_p, 'rb')
pdfReader = PyPDF2.PdfReader(file_handle)

page_number = len(pdfReader.pages)  # This tells you the total pages

frequency_table = {}
for page_num in range(page_number):
    page_object = pdfReader.pages[page_num]
    page_text = page_object.extract_text()  # this is the str type of full page
    words = page_text.split()
    for each_word in words:
        each_word.lower()
        if each_word in frequency_table:
            frequency_table[each_word] += 1
        else:
            frequency_table[each_word] = 1
    

print(frequency_table)
            

file_handle.close()
