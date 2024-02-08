from bs4 import BeautifulSoup
import  mammoth
from tkinter  import filedialog as fd

import prettifyxml
from prettifyxml import prettify
import zipfile
import xml.dom.minidom as xdm
# with (open('/Users/stanislavdidenko/Downloads/VRF подбор  Виллы V3-V6.docx','rb')as file):
#     zip = zipfile.ZipFile(file)
#     resfile = zip.extractall()
def openfile():
    filename=fd.askopenfilename()
    f = open(filename, 'rb')
    b = open('filename.html', 'wb')
    document = mammoth.convert_to_html(f)
    b.write(document.value.encode('utf8'))
    f.close()
    b.close()
    prettifyxml.prettify(b)






