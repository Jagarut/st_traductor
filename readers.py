import fitz  # PyMuPDF
import ebooklib
from ebooklib import epub
from pathlib import Path
from bs4 import BeautifulSoup

def get_file_reader(file_path):
    """Return appropriate reader function based on file extension"""
    extension = Path(file_path).suffix.lower()
    if extension == '.pdf':
        return read_pdf
    elif extension == '.epub':
        return read_epub
    elif extension in ['.txt', '.text']:
        return read_text
    else:
        raise ValueError(f"Unsupported file format: {extension}")

def read_pdf(file_path):
    """
    Reads a PDF file and extracts the text from each page.

    Parameters:
    file_path (str): The path to the PDF file.

    Returns:
    str: The extracted text from the PDF.
    """
    # Open the PDF document
    doc = fitz.open(file_path)
    text = ""

    # Iterate through each page in the document
    for page_num in range(len(doc)):
        # Load the page
        page = doc.load_page(page_num)
        # Extract the text from the page and append it to the text variable
        text += page.get_text()

    doc.close()
    return text


def read_epub(epub_path):
    """Extract plain text from EPUB file"""
    book = epub.read_epub(epub_path)
    text_content = []
    
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            # Get content and convert HTML to plain text
            content = item.get_content().decode('utf-8')
            soup = BeautifulSoup(content, 'html.parser')
            text = soup.get_text()
            # Remove extra whitespace
            text = ' '.join(text.split())
            text_content.append(text)
    
    return '\n\n'.join(text_content)

def read_text(file_path):
    """Extract text from plain text file"""
    with open(file_path, 'r', encoding='utf-8') as file:
        text_content = file.read()
    return text_content

