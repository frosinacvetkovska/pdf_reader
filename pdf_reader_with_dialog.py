from pypdf import PdfReader
import tkinter as tk
from tkinter import filedialog

def extract_text_from_pdf(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf, strict=False)
        pdf_text = []
        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)
        return pdf_text

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    
    pdf_file = filedialog.askopenfilename(
        title="Select PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )
    
    if pdf_file:
        extract_text = extract_text_from_pdf(pdf_file)
        for text in extract_text:
            print(text)
    else:
        print("No file selected.")