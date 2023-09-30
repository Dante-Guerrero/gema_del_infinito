import os
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader

# Path to the folder containing PDF files
input_folder = "input"

# Path to the folder where text files will be saved
output_folder = "output"

# Path to the Tesseract OCR executable (change if necessary)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Get a list of all PDF files in the input folder
files = [f for f in os.listdir(input_folder) if f.endswith(".pdf")]

# Loop through each PDF file and convert it to text using OCR
for file in files:
    pdf_path = os.path.join(input_folder, file)
    txt_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".txt")

    # Convert PDF pages to images
    images = convert_from_path(pdf_path)

    # Perform OCR on images and extract text
    text = ""
    for image in images:
        # text += pytesseract.image_to_string(image)
        text += pytesseract.image_to_string(image, lang='ron') # your document language

    # Save the extracted text to a text file
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)

print("Conversion complete!")