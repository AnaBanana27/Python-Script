"""
Traducción del Archivo PDF
Descripción: Traduce el contenido de un archivo PDF a otro idioma.
Prompt: "Traduce este archivo PDF al inglés."
"""

import PyPDF2
import google.generativeai as genai
from google.colab import userdata
import os

GOOGLE_API_KEY = "AIzaSyCbrZb34FBq3RXizIA9M9CPA7rre_PpX2A"
genai.configure(api_key=GOOGLE_API_KEY)

def translate_pdf_gemini(file_content):
    prompt = f"Traduce el siguiente archivo PDF al inglés:\n{file_content}"
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content(prompt)
    return response.text

def save_to_file(content, file_name="resultado_Script12.txt"):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)

with open("pdf.pdf", "rb") as file:
    pdf_reader = PyPDF2.PdfReader(file)
    file_content = ""
    for page in pdf_reader.pages:
        file_content += page.extract_text()

translation = translate_pdf_gemini(file_content)

save_to_file(translation)

print(translation)


