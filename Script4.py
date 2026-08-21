"""
Traducción
Descripción: Traduce un texto de un idioma a otro.
Prompt: "Traduce este texto del español al inglés: [Texto a traducir]."
"""

import google.generativeai as genai
from google.colab import userdata
import os

GOOGLE_API_KEY = ".............."
genai.configure(api_key=GOOGLE_API_KEY)

def translate_text_gemini(prompt):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content(prompt)
    return response.text

def save_to_file(content, file_name="resultado_Script10.txt"):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)

text = """¿Qué son los LLM?
Los modelos de lenguaje de gran tamaño (LLM) son una categoría de modelos fundacionales entrenados sobre enormes cantidades de datos que los hacen capaces de comprender y generar lenguaje natural, entre otros tipos de contenidos, para realizar una amplia gama de tareas.

Los LLM se han convertido en un nombre familiar gracias al papel que han desempeñado para llevar la IA generativa a la vanguardia del interés público. Además, las organizaciones se están enfocando en adoptar la inteligencia artificial en numerosas funciones comerciales y casos de uso.

Fuera del contexto empresarial, podría parecer que los LLM aparecieron de la nada junto con nuevos desarrollos en IA generativa. Sin embargo, muchas empresas, entre ellas IBM, han dedicado años a la implementación de estos modelos en diferentes niveles para mejorar sus capacidades de comprensión del lenguaje natural (NLU) y de procesamiento del lenguaje natural (NLP). Esto ha ocurrido junto con los avances en el aprendizaje automático, los modelos de aprendizaje automático, los algoritmos, las redes neuronales y los modelos de transformador que proporcionan la arquitectura para estos sistemas de IA.

Los LLM son una clase de modelo fundacional, que se entrena con enormes cantidades de datos para proporcionar las capacidades fundamentales necesarias para impulsar múltiples casos de uso y aplicaciones, así como resolver una multitud de tareas. Esto crea un marcado contraste con la idea de construir y entrenar modelos específicos de dominio para cada uno de estos casos de uso individualmente, lo cual es prohibitivo en función de muchos criterios (los más importantes son el costo y la infraestructura), sofoca las sinergias e incluso puede conducir a un menor rendimiento.

Los LLM representan un avance significativo en NLP e inteligencia artificial y son fácilmente accesibles para el público a través de interfaces como Chat GPT-3 y GPT-4 de OpenAI, que han obtenido el soporte de Microsoft. Otros ejemplos son los modelos Llama de Meta, las representaciones de codificadores bidireccionales de transformadores de Google (BERT/RoBERTa) y los modelos PaLM. Recientemente, IBM también lanzó su serie de modelos Granite en Watsonx.ai, que se ha convertido en la columna vertebral de la IA generativa para otros productos de IBM como watsonx Assistant y watsonx Orchestrate.

En pocas palabras, los LLM están diseñados para comprender y generar texto como un humano, además de otras formas de contenido, basándose en la enorme cantidad de datos utilizados para entrenarlos. Tienen la capacidad de inferir del contexto, generar respuestas coherentes y pertinentes para el contexto, traducir a idiomas distintos del inglés, resumir texto, responder preguntas (conversación general y preguntas frecuentes) e incluso ayudar en tareas de escritura creativa o de generación de código.

Pueden hacerlo gracias a miles de millones de parámetros que les permiten capturar patrones complejos en el lenguaje y realizar una amplia variedad de tareas relacionadas con el lenguaje. Los LLM están revolucionando las aplicaciones en varios campos, desde los chatbots y asistentes virtuales hasta la generación de contenido, asistencia para la investigación y traducción de idiomas.

Mientras continúan evolucionando y mejorando, los LLM están preparados para remodelar la forma en que interactuamos con la tecnología y accedemos a la información, lo que los convierte en una parte fundamental del panorama digital moderno."""

prompt = f"Traduce este texto del español al inglés:\n{text}"
output = translate_text_gemini(prompt)

save_to_file(output)

print(output)

