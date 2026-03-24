import sys

pdf_path = 'c:/Users/grifo/OneDrive/AI/VibeVoding/CAI/LV9/L04.pdf'

text = ""
try:
    import PyPDF2
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted: text += extracted + "\n"
    print("SUCCESS with PyPDF2")
except Exception as e:
    # print(f"PyPDF2 failed: {e}")
    try:
        import fitz # PyMuPDF
        doc = fitz.open(pdf_path)
        for page in doc:
            extracted = page.get_text()
            if extracted: text += extracted + "\n"
        print("SUCCESS with fitz")
    except Exception as e2:
        # print(f"fitz failed: {e2}")
        pass

with open('c:/Users/grifo/OneDrive/AI/VibeVoding/CAI/LV9/pdf_content.txt', 'w', encoding='utf-8') as f:
    f.write(text)
print("Wrote text length:", len(text))
