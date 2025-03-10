# pylint: skip-file
from rich.progress import Progress
import time
from PyPDF2 import PdfReader, PdfWriter
import argparse

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
def getPages(pdfFile):
    reader = PdfReader(pdfFile)
    pages = reader.pages
    return pages

def writeDocument(writer, pages):
    for page in pages:
        writer.add_page(page)

def MergePDF(pdfFiles):
    writer = PdfWriter()
    for file in pdfFiles:
        pages = getPages(file)
        writeDocument(writer, pages)
    with open("mergedPDF.pdf", "wb") as file:
        writer.write(file)


def encryptPDF(pdfFile, password: (str)):
    pages = getPages(pdfFile)
    writer = PdfWriter()
    for page in pages:
        writer.add_page(page)
    writer.encrypt(password)
    with open("encrypted_pdf.pdf", "wb") as file:
        writer.write(file)


def main():
    parser = argparse.ArgumentParser(description="Extract text from a PDF.")
    # parser.add_argument("fpath", type=str, help="Select output format (pdf or docx).")
    # parser.add_argument("password", type=str, help="Select output format (pdf or docx).")    
    parser.add_argument("-m", nargs = "*")
    args = parser.parse_args()
    
    MergePDF(args.m)

    #encryptPDF(f"{args.fpath}",f"{args.password}" )

if __name__ == "__main__":
    main()
