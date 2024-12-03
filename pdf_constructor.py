from fpdf import FPDF

def create_pdf_from_text(text: str, output_path: str, font_name: str = "Helvetica", font_size: int = 12) -> None:
    """
    Creates a PDF file from input text.
    
    Args:
        text: The text content to write to PDF
        output_path: The file path where PDF will be saved
        font_name: Name of the font to use (default: Helvetica)
        font_size: Size of the font (default: 12)
    """
    if not text or not output_path:
        raise ValueError("Text and output path must not be empty")
        
    pdf = FPDF()
    pdf.set_font('Helvetica', '', 12)
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font(font_name, size=font_size)
    
    # Calculate maximum width for text
    page_width = pdf.w - 2 * pdf.l_margin

    for line in text.split('\n'):
        # Use write instead of multi_cell for better text wrapping
        pdf.write(10, line + '\n')
        # Alternative: pdf.multi_cell(page_width, 10, line)

    try:
        pdf.output(output_path)
    except Exception as e:
        raise Exception(f"Failed to create PDF: {str(e)}")

