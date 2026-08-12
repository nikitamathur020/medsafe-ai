import pytesseract
from PIL import Image

def extract_text_from_image(image):
    """
    Extracts raw text from uploaded prescription images using Tesseract OCR.
    """
    try:
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return f"Error running OCR: {str(e)}. Make sure Tesseract is installed on your system."