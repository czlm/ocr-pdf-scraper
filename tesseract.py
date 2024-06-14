from PIL import Image
from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdf(pdf_file):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Chew\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    doc = convert_from_path(pdf_file, poppler_path=r"C:\Users\Chew\Downloads\Release-24.02.0-0\poppler-24.02.0\Library\bin")
    for page_number, page_data in enumerate(doc):
        txt = pytesseract.image_to_string(page_data).encode("utf-8")
        print("Page # {} - {}".format(str(page_number),txt))

        


if __name__ == '__main__':
    extract_text_from_pdf("TRM Guidelines 18 January 2021.pdf")
