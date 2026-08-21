"""
HTML / CSS
Descripción: Genera código para crear una página web sencilla con HTML y CSS.
Prompt: "Escribe el código HTML y CSS para una página web sobre LLM con un encabezado y un pie de página.
"""

import google.generativeai as genai
from google.colab import userdata
import os

GOOGLE_API_KEY = "AIzaSyCbrZb34FBq3RXizIA9M9CPA7rre_PpX2A"
genai.configure(api_key=GOOGLE_API_KEY)

def generate_html_css_gemini(prompt):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content(prompt)
    return response.text

def save_to_file(content, file_name="resultado_Script3.txt"):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)

prompt = "Escribe el código HTML y CSS para una página web sobre LLM con contenido, encabezado, un pie de página, etc."
output = generate_html_css_gemini(prompt)

save_to_file(output)

print(output)

