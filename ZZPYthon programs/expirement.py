from PyPDF2 import PdfFileMerger
def pdfcompiler(pdfs):
       merger = PdfFileMerger()
       for pdf in pdfs:
              merger.append(pdf)
       name = input("Please give a name for the combined PDF file (text only, no '.pdf'): ")
       merger.write(name + ".pdf")