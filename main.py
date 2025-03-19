# pylint: skip-file
from rich.progress import Progress
import time
from PyPDF2 import PdfReader, PdfWriter
import argparse
from pdf2docx import Converter
import os
import convertapi 

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


def MergePDF(pdfFiles, progress, task):
    writer = PdfWriter()
    for file in pdfFiles:
        pages = getPages(file)
        writeDocument(writer, pages)
    savePDF(writer, os.path.basename(pdfFiles[1]))
    progress.update(task, advance = 1)
    return os.path.basename(pdfFiles[1])


def encryptPDF(pdfFile, password: (str), progress, task):
    pages = getPages(pdfFile)
    writer = PdfWriter()
    writeDocument(writer, pages)
    writer.encrypt(password)
    print("{pdfFile} has been encrypted")
    savePDF(writer, "encrypted_PDF.pdf")
    progress.update(task, advance = 1)
    return "encrypted_PDF.pdf"

def decryptPDF(pdfFile, password: (str), progress, task):
    reader = PdfReader(pdfFile)
    writer = PdfWriter()
    if (reader.is_encrypted):
        reader.decrypt(password)
        writeDocument(writer, getPagesFromReader(reader))
    savePDF(writer, "decrypted_PDF.pdf")
    progress.update(task, advance = 1)
    return "decrypted_PDF.pdf"

def convertToWord(pdfFile, location, progress, task):
    os.path.basename(pdfFile)    
    cv = Converter(pdfFile)
    cv.convert(location)
    cv.close()
    progress.update(task, advance = 1)
    return location

def compressPDF(pdfFile, location, progress, task):
    convertapi.api_credentials = '' # <--- Enter Your convertAPI API Key here
    convertapi.convert('compress', {
    'File': pdfFile
    }, from_format = 'pdf').save_files(location)
    progress.update(task, advance = 1)
    return location

def main():

    parser = argparse.ArgumentParser(description="Extract text from a PDF.")
    parser.add_argument("-f", type=str, nargs="*", help="File Path(s) to process")
    parser.add_argument("-s", type=str, nargs="?", help="Optional Save Path")
    parser.add_argument("-e", type=str, help="Encryption Password")
    parser.add_argument("-m", action="store_true", help="Merge Documents")  
    parser.add_argument("-d", type=str, help="Decryption Password")  
    parser.add_argument("-c", action="store_true", help="Compress Document")  
    parser.add_argument("-w", action="store_true", help="Convert to Word Document")  

    args = parser.parse_args()
    output = args.s
    
    with Progress() as progress:
        totalTasks = sum([args.m, args.c, args.w, bool(args.e), bool(args.d)])

        if totalTasks == 0:
            print("Please imput some parameters to use this application")

        task = progress.add_task("[cyan]Processing...", total=totalTasks)

        if args.m:
            if args.f and len(args.f) >= 1:
                output = MergePDF(args.f, progress, task)
            else: print("Error: Provide pdfs or flag -f")

        if args.w:
            if args.f and len(args.f) == 1:
                output = convertToWord(args.f[0], args.s or "pdf2Word.docx", progress, task)
                print(output)
            else: print("Error: Too many PDF's inputted or flag -f missing")
        
        if args.c:
            if args.f and len(args.f) == 1:
                output = compressPDF(args.f[0], args.s or "CompressedPDf.pdf", progress, task)
            else: print("Error: Too many PDF's inputted or flag -f missing")
        
        if args.e:
            if args.m or args.w or args.c:
                output = encryptPDF(output, args.e, progress, task)
            elif args.f and len(args.f) == 1 and not (args.m or args.w or args.c):
                encryptPDF(args.f[0], args.e, progress, task)
            else: print("Error: Incorrect flags provided")

        if args.d:
            if args.f and len(args.f) == 1:
                output = decryptPDF(args.f[0], args.d, progress, task)
            else: print("Error: Too many PDF's inputted or flag -f missing")



if __name__ == "__main__":
    main()
