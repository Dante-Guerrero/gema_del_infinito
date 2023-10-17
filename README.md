# TesseractoEnDFI
Uso del Tesseract como herramienta de reconocimiento óptico de caracteres (OCR) que convierte imágenes de texto en texto editable y buscable.

### Instrucciones para usar Tesseract (y que funcione)

Ésta es la web de la librería: https://pypi.org/project/pytesseract/

1) Primer paso: instalar Tesseract. 
   - La web para la instalación se encuentra en: https://tesseract-ocr.github.io/tessdoc/Installation.html 
     Ir hasta la parte final (buscar "Windows"). 
   - Identificar el enlace "Tesseract at UB Mannheim", lleva a: https://github.com/UB-Mannheim/tesseract/wiki
   - Descargar con el enlace bajo el título "latest installer". 
   - Instalar. 

2) Agregar idiomas (especialmente el español).
   - Web de idiomas: https://tesseract-ocr.github.io/tessdoc/Data-Files.html
   - Clonar el repositorio: https://github.com/tesseract-ocr/tessdata_best
   - Identificar el archivo "spa.traineddata" y copiar.
   - Pegar en la carpeta "tessdata", que normalmente estará en C:\Program Files\Tesseract-OCR\tessdata

3) Instalar la librería "pytesseract"
   - En el cmd correr: pip install pytesseract

4) Correr un primer código.
   - Ver el hilo en stack overflow: https://stackoverflow.com/questions/66995340/pdf-to-text-convert-using-python-pytesseract
   - Ubicar el ejemplo del usuario "Just me".
   - Para correr este ejemplo se requiere adicionalmente lo siguiente:
     -> Instalar con pip: PILLOW, pdf2image y PyPDF2
     -> pdf2image requiere además que se instale "poppler".
     -> descargar poppler de: https://github.com/oschwartz10612/poppler-windows/releases/tag/v23.08.0-0
     -> se instala copiando la carpeta "Release" en C:\Program Files
     Inicialmente me arroja un error, pero hice un cambio:
     -> en la variable "images", creada con la función "convert_from_path", agregué un argumento.
     -> queda así:
     "images = convert_from_path(pdf_path, poppler_path=r'C:\Program Files\poppler-23.08.0\Library\bin')"

### Otros enlaces de interés

- https://stackoverflow.com/questions/66995340/pdf-to-text-convert-using-python-pytesserac
