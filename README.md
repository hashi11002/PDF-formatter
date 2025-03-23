 # PDF Formatter
This tool allows you to perform multiple operations such as merging, and encrypting on your PDF's using one command line.

## API's and libraries imported
  Rich <br>
  PyPDF2<br>
  Argparse<br>
  PDf2Docx<br>
  os<br>
  ConvertAPI<br>
  
  
  

## Install Guide

**Windows Install Guide:**
1) Clone project into your code editor
2) Open terminal, navigate to your local repository and install virtual environment on your computer with the command: <br> <br>
  
   ```
   pip install virtualenv
   ```
   
   <br>
   
3) Create a virtual enviroment instance with the command(You can replace myenv with any name for your environment):<br><br>
    
    ```
     python -m venv myenv
    ```
    
    <br>

4) Run command to activate your virtual environment(replace myenv with your virtual environment name):<br><br>

   ``` 
   myenv\Scripts\activate
   ```
   
   <br>
   
5) Install all the libraries needed by the application: <br><br>
    
    ```
    pip install -r requirements.txt
    ```

   <br>
   
6) Get the API Key for the file compressor from [here](https://www.convertapi.com/pdf-to-compress/python) and add it in the .env class with the variable API_KEY.
7) Now you are able to run the application. Enjoy :)

<br>

**Mac OS Intall Guide:**
1) Clone the project into your code editor.
2) Open Terminal, navigate to your local repository, and install virtual environment with the command:<br><br>

   ```
   pip install virtualenv
   ```
  <br>
  
3) Create a virtual environment instance with the command (You can replace myenv with any name you would like for your environment):<br><br>

   ```
   python3 -m venv myenv
   ```

   <br>
4) Activate your virtual environment with the command:<br><br>

   ```
   source myenv/bin/activate
   ```

   <br>
5) Install all the libraries needed by the application: <br><br>

    ```
    pip install -r requirements.txt
    ```

    <br>
   
6) Get the API Key for the file compressor from [here](https://www.convertapi.com/pdf-to-compress/python) and add it in the .env class with the variable API_KEY.
7) Now you are able to run the application. Enjoy :)


## Flag Guide
This project uses argument passer library to allow the user to perform any operation on their PDF's. The Flags are as follows:
  - -f : List of file(s) paths that need the operation <br>
  - -s : Location and name of the file to save as <br>
  - -e : Password to encrypt the file with <br>
  - -m : Boolean flag that triggers merging of PDF's <br>
  - -d : Passsword to decrypt the file with <br>
  - -c : Boolean flag that triggers compression of PDF File <br>
  - -w : Boolean flag that triggers conversion of PDF File to Word Document <br>

## Order of operations
The order is as follows from top to bottom:
- merge PDF
- Convert PDF to Word
- Compress PDF
- Encrypt PDF
- Decrypt PDF

## Simple Use Case examples
You can try simple commands in your terminal that perform a single operation as follows: 

-  #### To Merge 2 PDF's and save it with a name you specify:<br>
```
  python main.py -m -f "path\to\your\pdf1" "path\to\your\pdf2" -s 'merged-pdf.pdf'
```
<br>
-  #### To Encrypt a PDF:<br>
 ```
  python main.py -f "path\to\your\pdf" -e 'password-to-encrypt-with'
 ``` 
   <br>
- #### To convert a PDF to a Word Document:<br>
  ```
  python main.py -f "path\to\your\pdf" -w
  ``` 
   <br>
- #### To decrypt a file:<br>
  ```
  python main.py -f "path\to\your\encrypted\pdf" -d 'password-to-decrypt-with'
  ```
   <br>
- #### To compress a PDF file:<br>
  ```
  python main.py -f "path\to\your\pdf" -c
  ``` 
 <br>
## Complex Use Case Examples

- #### Merging and encrypting PDF files:<br>
```
  python main.py -m -f "path\to\your\pdf" "path\to\your\pdf" -s "output-pdf.pdf" -e "password-to-encrypt-with"
```
<br>

-  #### Merging and converting to word document and saving it with a name:<br>
  ```
  python main.py -m -f "path\to\your\pdf1" "path\to\your\pdf2" -w -s mergeddocs.docx
 ```
 <br>
  
