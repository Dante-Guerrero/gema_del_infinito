import os
import shutil
import pytesseract
import pandas as pd
from PIL import Image
from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader

# Path to the folder containing PDF files
input_folder = "input"

# Path to the folder where text files will be saved
output_folder = "output"

# Path to the Tesseract OCR executable (change if necessary)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# defining the function to ignore the files
# if present in any folder
def ignore_files(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]
 
# calling the shutil.copytree() method and
# passing the src,dst,and ignore parameter
shutil.copytree(input_folder,
                output_folder,
                ignore=ignore_files, 
                dirs_exist_ok=True)

# Get a list of all PDF files in the input folder
archivos = []
for path, subdirs, files in os.walk(input_folder):
    for name in files:
        archivos.append(os.path.join(path, name))

# Loop through each PDF file and convert it to text using OCR
for archivo in archivos:
    pdf_path = archivo
    archivo_n = archivo[len(input_folder):]
    txt_path = output_folder + os.path.splitext(archivo_n)[0] + ".txt"

    # Convert PDF pages to images
    images = convert_from_path(pdf_path, poppler_path=r'C:\Program Files\poppler-23.08.0\Library\bin') # Descargar poppler de: https://github.com/oschwartz10612/poppler-windows/releases/tag/v23.08.0-0
    # Perform OCR on images and extract text
    text = ""
    for image in images:
        # text += pytesseract.image_to_string(image)
        text += pytesseract.image_to_string(image, lang='spa') # Descargar el lenguaje en: https://github.com/tesseract-ocr/tessdata_best

    # Save the extracted text to a text file
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)

print("Conversion complete!")