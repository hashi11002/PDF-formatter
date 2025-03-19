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
  -f : List of file(s) paths that need the operation. 
  -s : Location and name of the file to save as.
  -e : Password to encrypt the file with.
  -m : Boolean flag that triggers merging of PDF's.
  -d : Passsword to decrypt the file with.
  -c : Boolean flag that triggers compression of PDF File.
  -w : Boolean flag that triggers conversion of PDF File to Word Document.

  ## Use Case examples
  You can try simple commands in your terminal that perform a single operation as follows: 

  
