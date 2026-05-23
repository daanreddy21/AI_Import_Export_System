import fitz  
def extract_text_from_pdf(file_path):
    text = ""
    pdf_document = fitz.open(file_path)
    for page in pdf_document:
        text += page.get_text()
    pdf_document.close()

    return text

# import fitz
# import pdfplumber
# def extract_text_from_pdf(pdf_path):
#     full_text = ""
#     doc = fitz.open(pdf_path)
#     for page in doc:
#         text = page.get_text()
#         full_text += text + "\n"
#     doc.close()
#     try:
#         with pdfplumber.open(pdf_path) as pdf:
#             for page in pdf.pages:
#                 tables = page.extract_tables()
#                 for table in tables:
#                     for row in table:
#                         row_text = " | ".join(
#                             [
#                                 str(cell)
#                                 for cell in row
#                                 if cell
#                             ]
#                         )
#                         full_text += row_text + "\n"
#     except Exception as e:
#         print(
#             "Table Extraction Error:",
#             e
#         )
#     return full_text