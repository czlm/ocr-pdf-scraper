# Installation

## Packages

```
pip install -r requirements.txt

```

## Windows

**Poppler**

Windows users will have to build or download poppler for Windows, https://github.com/oschwartz10612/poppler-windows/releases/.  You will then have to add the ```bin/``` folder to PATH or use ```poppler_path = r"C:\path\to\poppler-xx\bin"``` as an argument in convert_from_path.

**Pytesseract**

https://github.com/UB-Mannheim/tesseract/wiki

Set tesseract path in the script before calling image_to_string

```
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
```