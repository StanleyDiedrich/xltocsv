from bs4 import BeautifulSoup
import getdatas

def prettify(file):
    filename=file.name
    resname="resfile.html"
    with (open(filename, 'r') as file):
        soup =BeautifulSoup(file,'html.parser')

    with (open(resname,"w")as rfile):
        rfile.write(soup.prettify())
        getdatas.createFCU()