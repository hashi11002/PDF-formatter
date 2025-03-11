# pylint: skip-file
from rich.progress import Progress
import time
from PyPDF2 import PdfReader, PdfWriter
import argparse
from pdf2docx import Converter
import os

'''
CLI progress bar
'''
with Progress() as progress:
    task = progress.add_task("[cyan]Processing...", total=10)
    for i in range(10):
        time.sleep(0.1)  # Simulating work
        progress.update(task, advance=1)

'''
Helper Method:
Reads a PDF file and converts it into pages that can be used 
by the PYPDF2 library
''' 
def getPages(pdfFile: (str)):
    reader = PdfReader(pdfFile)
    pages = reader.pages
    return pages

def getPagesFromReader(reader: (PdfReader)):
    pages = reader.pages
    return pages


def savePDF(writer, name: (str)):
    with open(name, "wb") as file:
        writer.write(file)


def writeDocument(writer, pages):
    for page in pages:
        writer.add_page(page)


def MergePDF(pdfFiles):
    writer = PdfWriter()
    for file in pdfFiles:
        pages = getPages(file)
        writeDocument(writer, pages)
    savePDF(writer, os.path.basename(pdfFiles[1]))


def encryptPDF(pdfFile, password: (str)):
    pages = getPages(pdfFile)
    writer = PdfWriter()
    writeDocument(writer, pages)
    writer.encrypt(password)
    savePDF(writer, "encrypted_PDF.pdf")

def decryptPDF(pdfFile, password: (str)):
    reader = PdfReader(pdfFile)
    writer = PdfWriter()
    if (reader.is_encrypted):
        reader.decrypt(password)
        writeDocument(writer, getPagesFromReader(reader))
    savePDF(writer, "decrypted_PDF.pdf")

def convertToWord(pdfFile, location = "pdf2word.docx"):
    os.path.basename(pdfFile)    
    cv = Converter(pdfFile)
    cv.convert(location)
    cv.close()



def main():
    parser = argparse.ArgumentParser(description="Extract text from a PDF.")
    #parser.add_argument("fpath", type=str)
    #parser.add_argument("spath", type=str, nargs = "?")  
    #parser.add_argument("password", type=str, nargs = "?")    
    parser.add_argument("-m", nargs = "*")
    args = parser.parse_args()
    
    MergePDF(args.m)

    #convertToWord(args.fpath,args.spath)

if __name__ == "__main__":
    main()
