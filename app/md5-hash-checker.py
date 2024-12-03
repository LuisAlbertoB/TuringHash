import tkinter as tk
import re

def is_md5_hash(input_str):
    """
    Verifica si una cadena de texto es un hash MD5 válido.
    
    Parámetros:
    input_str (str): Cadena de texto a validar.
    
    Devuelve:
    bool: True si es un hash MD5 válido, False en caso contrario.
    """
    # Patrón regular para validar un hash MD5
    md5_pattern = r'^[0-9a-f]{32}$'
    
    # Comprobar si la cadena de texto cumple con el patrón
    return bool(re.match(md5_pattern, input_str))

def check_hash():
    """
    Función que se ejecuta al hacer clic en el botón.
    Verifica si el texto ingresado es un hash MD5 válido y
    muestra el resultado en la etiqueta.
    """
    input_text = entry.get()
    if is_md5_hash(input_text):
        label.config(text="¡Es un hash MD5 válido!")
    else:
        label.config(text="No es un hash MD5 válido.")

# Crear la ventana principal
root = tk.Tk()
root.title("Verificador de Hash MD5")

# Crear el campo de entrada
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Crear el botón
button = tk.Button(root, text="Verificar", command=check_hash)
button.pack(pady=10)

# Crear la etiqueta para mostrar el resultado
label = tk.Label(root, text="")
label.pack(pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()
