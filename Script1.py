"""
Conversión a JSON
Descripción: Convierte texto o datos a formato JSON.
Prompt: "Convierte el siguiente texto en un objeto JSON."
"""

import google.generativeai as genai
from google.colab import userdata
import os

GOOGLE_API_KEY = "AIzaSyCbrZb34FBq3RXizIA9M9CPA7rre_PpX2A"
genai.configure(api_key=GOOGLE_API_KEY)

def convert_to_json_gemini(prompt):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content(prompt)
    return response.text

def save_to_file(content, file_name="resultado_Script5.txt"):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)

prompt = """Convierte el siguiente texto en un objeto JSON: Juan Pérez es un ingeniero de software de 29 años que vive en Calle Falsa 123, 
en Madrid, España. Desde muy joven, mostró un gran interés por la tecnología y la programación, lo que lo llevó a estudiar Ingeniería Informática 
en la universidad. Después de graduarse, comenzó a trabajar en el desarrollo de aplicaciones web y ha acumulado más de cinco años de experiencia 
en el campo. Durante este tiempo, ha adquirido habilidades en varias tecnologías, incluyendo Python, JavaScript y bases de datos SQL, lo que le 
ha permitido participar en numerosos proyectos de software innovadores. Juan es conocido por su capacidad para resolver problemas complejos y 
su atención al detalle. Además de su trabajo, se puede contactar con él a través de su correo electrónico, juan.perez@example.com, o su número 
de teléfono, +34 600 123 456. Fuera del trabajo, Juan disfruta de varios hobbies que le permiten relajarse y recargar energías. Le apasiona la 
programación, ya que siempre está buscando nuevas formas de mejorar sus habilidades y aprender tecnologías emergentes. También es un ávido lector, 
disfrutando de novelas de ciencia ficción y libros sobre desarrollo personal. Por último, le gusta practicar senderismo los fines de semana, 
explorando la naturaleza y desconectando de la rutina diaria. Estas actividades no solo le brindan placer, sino que también contribuyen a su
 bienestar general y equilibrio entre trabajo y vida personal."""

output = convert_to_json_gemini(prompt)

save_to_file(output)

print(output)

