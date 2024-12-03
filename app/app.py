from flask import Flask, request, jsonify, render_template
import hashlib
import itertools
import string
import re
import os

app = Flask(__name__)

def is_md5_hash(input_str):
    md5_pattern = r'^[0-9a-f]{32}$'
    return bool(re.match(md5_pattern, input_str))

def fuerza_bruta_md5(hash_objetivo, longitud_maxima=5):
    caracteres = string.ascii_letters + string.digits
    for longitud in range(1, longitud_maxima + 1):
        for combinacion in itertools.product(caracteres, repeat=longitud):
            texto_prueba = ''.join(combinacion)
            hash_prueba = hashlib.md5(texto_prueba.encode('utf-8')).hexdigest()
            if hash_prueba == hash_objetivo:
                return texto_prueba
    return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_hash():
    data = request.json
    input_text = data.get("hash")

    if not is_md5_hash(input_text):
        return jsonify({"message": "No es un hash MD5 válido.", "success": False})

    resultado = fuerza_bruta_md5(input_text)
    if resultado:
        return jsonify({"message": f"¡Texto encontrado! El texto es: {resultado}", "success": True})
    else:
        return jsonify({"message": "No se pudo descifrar el texto en el rango especificado.", "success": False})

if __name__ == '__main__':
    app.run(debug=True)
