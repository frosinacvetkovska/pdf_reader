from pypdf import PdfReader

def extract_text_from_pdf(pdf_file : str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf, strict=False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

        return pdf_text

if __name__ == '__main__':
    pdf_file = input("Enter PDF file path: ")
    extract_text = extract_text_from_pdf(pdf_file)
    
    for text in extract_text:
        print(text)
