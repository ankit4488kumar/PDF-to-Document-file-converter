from pdf2docx import parse

pdf_file = "C:/Users/ankit/Downloads/MULTI_THREADING_AND_SHARED_MEMORY_POOL_T.pdf"
word_file = "C:/Users/ankit/Downloads/MULTI_THREADING_AND_SHARED_MEMORY_POOL_T.docx"
parse(pdf_file, word_file, start=0, end=None)
print("PDF file has been converted into Docx")