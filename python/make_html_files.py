# Este script crea archivos según una lista de nombres proporcionada.

import os

# Lista de nombres de archivos
nombres_archivos = [
    "./pages/about.html",
    "./pages/services.html",
    "./pages/contact.html",
    "./pages/blog.html",
]

Title_html = [
    "Sobre nosotros",
    "Nuestros servicios",
    "Contáctanos",
    "Blog",
]
main_content_file = [
    "about.html",
    "services.html",
    "contact.html",
    "blog.html",
] 
    
# Ruta correcta del archivo HTML por defecto
default_html_path = "./python/deaful.html"  # Ajusta la ruta según la ubicación real del archivo
main_content_path = "./python/body-pages/"

# Leer el contenido del armain_content_filechivo HTML por defecto
with open(default_html_path, 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()

# Crear el directorio si no existe
directorio = "./pages"
if not os.path.exists(directorio):
    os.makedirs(directorio)
print(f"Directorio creado: {directorio}")

# Crear un archivo HTML básico para cada nombre en la lista
for nombre, title, parrafo in zip(nombres_archivos, Title_html, main_content_file):
    print(f"Creando archivo: {nombre}")
    with open(main_content_path + parrafo, 'r', encoding='utf-8') as archivo:
        parrafo = archivo.read()  # Leer el contenido del archivo <main>
    with open(nombre, 'w', encoding='utf-8') as archivo:
        # Reemplazar las variables en la plantilla
        contenido_personalizado = contenido.replace("${title}", title)
        contenido_personalizado = contenido_personalizado.replace("${page_title}", title)
        contenido_personalizado = contenido_personalizado.replace("${content}", parrafo)
        
        # Escribir el contenido personalizado en el archivo
        archivo.write(contenido_personalizado)
    print("Archivos creados con éxito."
          , "ubicación de los archivos: ", os.path.abspath(directorio))