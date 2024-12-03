import hashlib
import itertools
import string
import re
import tkinter as tk


def is_md5_hash(input_str):

    md5_pattern = r'^[0-9a-f]{32}$'  # Patrón regular para validar un hash MD5
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


def process_hash():
    
    input_text = entry.get()
    
    if not is_md5_hash(input_text):
        label_result.config(text="No es un hash MD5 válido.")
        return
    
    label_result.config(text="Es un hash MD5 válido. Intentando descifrar...")
    root.update()  

    resultado = fuerza_bruta_md5(input_text)
    if resultado:
        label_result.config(text=f"¡Texto encontrado! El texto es: {resultado}")
    else:
        label_result.config(text="No se pudo descifrar el texto en el rango especificado.")


root = tk.Tk()
root.title("Hash MD5 Verificador y Descifrador")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

button = tk.Button(root, text="Procesar", command=process_hash)
button.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()
