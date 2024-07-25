# Text-to-Speech PDF Reader

This Python script utilizes the PyPDF2 and pyttsx3 libraries to convert the text content of a PDF file into spoken audio.

## Dependencies:

- **PyPDF2:** Used for extracting text from PDF documents. Install it using `pip install PyPDF2`.
- **pyttsx3:** Enables text-to-speech conversion. Install it using `pip install pyttsx3`.
- **tkinter:** Provides a graphical interface for file selection (optional, but recommended). Install it using `pip install tkinter`.

## Setting Up a Virtual Environment (Recommended):

1. Create a virtual environment using your preferred method (e.g., `venv`, `virtualenv`).
2. Activate the environment:
   - **Windows:** `venv\Scripts\activate`
   - **macOS/Linux:** `source venv/bin/activate`
3. Install the required dependencies within the activated environment using `pip install <package_name>`.

## Running the Script:

1. Save the script as `pdf_to_speech.py` (or any preferred name with the `.py` extension).
2. Open a terminal or command prompt and navigate to the directory where you saved the script.
3. Run the script using the following command:

   ```bash
   python pdf_to_speech.py
