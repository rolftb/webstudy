# Este script crea archivos según una lista de nombres proporcionada.

import os

# Lista de nombres de archivos
nombres_archivos = [
"./pages/about.html",
"./pages/team.html",
"./pages/history.html",
"./pages/services.html",
"./pages/wellness.html",
"./pages/appointments.html",
"./pages/emergencies.html",
"./pages/euthanasia.html",
"./pages/testimonials.html",
"./pages/contact.html",
"./pages/blog.html",
]
Title_html = [
"Sobre nosotros",
"Nuestro equipo",
"Nuestra historia",
"Nuestros servicios",
"Bienestar animal",
"Reservas",
"Emergencias",
"Proceso de eutanasia",
"Testimonios",
"Contáctanos",
"Blog",
]

parrafos_main = [
    "<p>Bienvenido a nuestra clínica veterinaria, donde el bienestar de tu mascota es nuestra prioridad. Contamos con un equipo de profesionales dedicados a brindar la mejor atención.</p>",
    "<p>Conoce a nuestro equipo de veterinarios y especialistas que están aquí para cuidar de la salud de tu mascota.</p>",
    "<p>Nuestra historia comienza con una pasión por los animales y un compromiso con su bienestar. Descubre cómo hemos crecido y evolucionado a lo largo de los años.</p>",
    "<p>Ofrecemos una amplia gama de servicios para garantizar la salud y felicidad de tu mascota. Desde chequeos regulares hasta tratamientos especializados.</p>",
    "<p>Nuestros planes de bienestar están diseñados para mantener a tu mascota saludable y feliz. Infórmate sobre nuestras opciones.</p>",
    """
    <p>Reserva una cita con nosotros de manera fácil y rápida. Estamos aquí para ayudarte a cuidar de tu mascota.</p>
    <p>Consulta nuestros precios y servicios para asegurarte de que tu mascota reciba la mejor atención posible.</p>
    <form action="https://example.com/submit" method="POST">
        <label for="name">Nombre:</label>
        <input type="text" id="name" name="name" required>
        <label for="email">Correo electrónico:</label>
        <input type="email" id="email" name="email" required>
        <label for="phone">Teléfono:</label>
        <input type="tel" id="phone" name="phone" required>
        <label for="message">Mensaje:</label>
        <textarea id="message" name="message" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    <p>En caso de emergencia, estamos disponibles para ayudarte. No dudes en contactarnos.</p> 
    """,
    """
    <p>La eutanasia es una decisión difícil. Estamos aquí para guiarte y ofrecerte el apoyo que necesitas en este momento.</p>
    <p>Lee los testimonios de nuestros clientes satisfechos y descubre por qué somos la mejor opción para el cuidado de tu mascota.</p>
    """,
    """
    <p>Contáctanos para cualquier consulta o pregunta. Estamos aquí para ayudarte.</p>
    <p>Visita nuestro blog para obtener consejos, noticias y artículos sobre el cuidado de mascotas.</p>
    """,
    """
    <p>Bienvenido a nuestro blog, donde compartimos consejos y noticias sobre el cuidado de mascotas.</p>
    <p>Explora nuestros artículos y mantente informado sobre las últimas tendencias en el cuidado de animales.</p>
    """,
]
    
    


# Crear el directorio si no existe
directorio = "./pages"
if not os.path.exists(directorio):
    os.makedirs(directorio)
print(f"Directorio creado: {directorio}")
# Crear un archivo HTML básico para cada nombre en la lista
for nombre, title, parrafo in zip(nombres_archivos, Title_html, parrafos_main):
    print(f"Creando archivo: {nombre}")
    with open(nombre, 'w', encoding='utf-8') as archivo:
        # Escribir contenido HTML básico
        contenido = f"""
"""
        archivo.write(contenido)
    print("Archivos creados con éxito."
          , "ubicación de los archivos: ", os.path.abspath(directorio))