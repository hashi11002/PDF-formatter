# PDF Formatter
This tool allows you to perform multiple operations such as merging, and encrypting on your PDF's using one command line.

## Install Guide

Windows Install Guide:
1) Clone project into your code editor
2) Open terminal, navigate to your local repository and install virtual environment on your computer with the command : pip install virtualenv
3) Create a virtual enviroment instance with the command :  python -m venv myenv (You can replace myenv with any name you would like for your environment)
4) Run command to activate your virtual environment : myenv\Scripts\activate (replace myenv with your virtual environment name)
5) Install all the libraries needed by the application : pip install rich PyPDF2 pdf2docx convertapi argparse
6) Now you are able to run the application. Enjoy :)


## Flag Guide
This project uses argument passer library to allow the user to perform any operation on their PDF's. The Flags are as follows:
  - -f : List of file(s) paths that need the operation <br>
  - -s : Location and name of the file to save as <br>
  - -e : Password to encrypt the file with <br>
  - -m : Boolean flag that triggers merging of PDF's <br>
  - -d : Passsword to decrypt the file with <br>
  - -c : Boolean flag that triggers compression of PDF File <br>
  - -w : Boolean flag that triggers conversion of PDF File to Word Document <br>

  ## Use Case examples
  You can try simple commands in your terminal that perform a single operation as follows: 

  - #### To Merge 2 PDF's and save it with a name you specify:<br>
  <br>
python main.py -m -f '..PDF formatter\samplepdf\samplepdf2mb.pdf' '..\PDF formatter\samplepdf\samplepdf3mb.pdf' -s 'merged-pdf.pdf'

 - #### To Encrypt a PDF:<br>
 <br>
  python main.py -f '..\PDF formatter\samplepdf\samplepdf2mb.pdf' -e 'password-to-encrypt-with'
  
  - #### To convert a PDF to a Word Document:<br>
 <br>
  python main.py -f '..\Path-to-your-pdf' -w
  
  - #### To decrypt a file:<br>
  <br>
  python main.py -f '..\path-to-your-encrypted-file.pdf' -d 'password-to-decrypt-with'
  
  - #### To compress a PDF file:<br>
  <br>
  python main.py -f '..\path-to-your-pdf-file.pdf' -c

  
