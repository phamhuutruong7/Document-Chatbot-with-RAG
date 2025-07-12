import fitz  # PyMuPDF
from docx import Document
import io

def parse_file(uploaded_file):
    """
    Parse uploaded file and extract text content
    
    Args:
        uploaded_file: Streamlit uploaded file object
        
    Returns:
        str: Extracted text content
    """
    file_extension = uploaded_file.name.lower().split('.')[-1]
    
    if file_extension == 'pdf':
        return parse_pdf(uploaded_file)
    elif file_extension == 'docx':
        return parse_docx(uploaded_file)
    elif file_extension == 'txt':
        return parse_txt(uploaded_file)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")

def parse_pdf(uploaded_file):
    """
    Extract text from PDF file
    
    Args:
        uploaded_file: Streamlit uploaded file object
        
    Returns:
        str: Extracted text content
    """
    try:
        # Read the uploaded file bytes
        pdf_bytes = uploaded_file.read()
        
        # Open PDF document
        pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
        
        text_content = ""
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text_content += page.get_text()
            text_content += "\n\n"  # Add page separator
        
        pdf_document.close()
        return text_content.strip()
        
    except Exception as e:
        raise Exception(f"Error parsing PDF: {str(e)}")

def parse_docx(uploaded_file):
    """
    Extract text from DOCX file
    
    Args:
        uploaded_file: Streamlit uploaded file object
        
    Returns:
        str: Extracted text content
    """
    try:
        # Read the uploaded file bytes
        docx_bytes = uploaded_file.read()
        
        # Open DOCX document
        document = Document(io.BytesIO(docx_bytes))
        
        text_content = ""
        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                text_content += paragraph.text + "\n"
        
        return text_content.strip()
        
    except Exception as e:
        raise Exception(f"Error parsing DOCX: {str(e)}")

def parse_txt(uploaded_file):
    """
    Extract text from TXT file
    
    Args:
        uploaded_file: Streamlit uploaded file object
        
    Returns:
        str: Extracted text content
    """
    try:
        # Read the uploaded file as text
        text_content = uploaded_file.read().decode('utf-8')
        return text_content.strip()
        
    except UnicodeDecodeError:
        # Try with different encoding if UTF-8 fails
        try:
            uploaded_file.seek(0)
            text_content = uploaded_file.read().decode('latin-1')
            return text_content.strip()
        except Exception as e:
            raise Exception(f"Error parsing TXT file with encoding: {str(e)}")
    except Exception as e:
        raise Exception(f"Error parsing TXT: {str(e)}")

def extract_sections(text_content, file_type='txt'):
    """
    Extract section headers from document content
    
    Args:
        text_content (str): Document text content
        file_type (str): Type of file (pdf, docx, txt)
        
    Returns:
        list: List of section headers
    """
    sections = []
    lines = text_content.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Simple heuristics for section detection
        # Look for numbered sections, headers with specific patterns
        if (
            line.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')) or
            line.startswith(('Chapter', 'Section', 'Part')) or
            (len(line) < 100 and line.isupper()) or
            (line.startswith('#') and file_type == 'txt')  # Markdown headers
        ):
            sections.append(line)
    
    return sections