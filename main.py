import PyPDF2
import pyttsx3
import tkinter as tk 
from tkinter import filedialog

def read_pdf_pages(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # speed
    engine.setProperty('volume', 0.9)  # volume

    for page_number, page in enumerate(pdf_reader.pages):
        text = page.extract_text()
        engine.say(text)
        engine.runAndWait()
        print(f"Reading page {page_number+1}")

def select_pdf_file():

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title= 'Select PDF File',
        filetypes=[("PDF Files", "*.pdf")])
    
    return file_path


pdf_file = select_pdf_file()
if pdf_file:
    read_pdf_pages(pdf_file)
else:
    print('No file selected.')
