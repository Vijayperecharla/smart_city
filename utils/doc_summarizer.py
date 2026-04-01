from PyPDF2 import PdfReader
import tempfile
import os

def extract_text_from_pdf(file_path):
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text

def summarize_text(text):
    sentences = text.split(".")
    summary = ".".join(sentences[:3])
    return summary.strip()

def summarize_document(file):
    try:
        if file.type == "application/pdf":
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                tmp.write(file.read())
                tmp_path = tmp.name

            text = extract_text_from_pdf(tmp_path)
            os.remove(tmp_path)
        else:
            text = file.read().decode("utf-8")

        if not text.strip():
            return "No readable content found."

        return summarize_text(text)

    except Exception as e:
        return f"Error: {str(e)}"
