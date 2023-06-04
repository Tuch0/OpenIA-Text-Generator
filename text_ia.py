# Importamos las librerias
import os
import openai
import json
import re
from sys import stdout

# Term Colours
def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)

# Varibles openai
openai.organization = "<your-token-openia-organization>"
openai.api_key = "<your-api-key>"


# Contenido de el texto
with open('test.txt')as file:
    for line in file:
        green()
        print(line)
        white()
        line = str(line)
        prompt = line

        # Añadiendo parámetros
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.4,
            max_tokens=200
        )



        # Imprimimos la respuesta
        text = response['choices'][0]['text']
        text = re.sub("\n","",text)

        # Imprimimos la clave por pantalla
        print(text)
    
    #print("\n")