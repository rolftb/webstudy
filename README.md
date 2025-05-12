# webstudy
## Descripción

Este repositorio está destinado a estudiar HTML y sus funciones como CSS y otras tecnologías web. Aquí encontrarás ejemplos, ejercicios y recursos para mejorar tus habilidades en desarrollo web.

## Requisitos

Para trabajar con este repositorio necesitas tener instalado **Node.js**.  
Puedes instalarlo fácilmente usando [Homebrew](https://brew.sh/) en macOS.

Si no tienes Homebrew instalado, puedes instalarlo ejecutando este comando en la terminal:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Luego instala Node.js con:
```bash
brew install node
```

También puedes descargar Node.js directamente desde [nodejs.org](https://nodejs.org/).

Después de instalar Node.js, instala Sass globalmente con npm:
```bash
npm install -g sass
```

### Versiones utilizadas

- Node.js: 20.x
- npm: 10.9.2
- Sass: 1.77.x

### Actualización de npm

Es posible que al instalar paquetes veas un mensaje como este:

```
npm notice New major version of npm available! 10.9.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
```

Si deseas actualizar npm a la última versión recomendada, ejecuta:

```bash
npm install -g npm@11.3.0
```

## Contenido

- **HTML**: Estructura básica, etiquetas, atributos, formularios, tablas, etc.
- **CSS**: Selectores, propiedades, diseño responsivo, flexbox, grid, etc.
- **JavaScript**: Manipulación del DOM, eventos, funciones, etc.
- **Recursos adicionales**: Enlaces a documentación, tutoriales y herramientas útiles.

## Generación automática de páginas HTML

Este repositorio incluye un script en Python llamado `make_html_files.py` que permite construir varias de las páginas HTML del sitio de forma automática a partir de plantillas y archivos de contenido.

### ¿Cómo funciona?

- El script toma una plantilla base (`python/deaful.html`) y reemplaza variables como `${title}`, `${page_title}` y `${content}`.
- El contenido principal de cada página se encuentra en archivos individuales dentro de la carpeta `python/body-pages/`.
- Los archivos HTML generados se guardan en la carpeta `pages/`.

### ¿Cómo usarlo?

1. Asegúrate de tener Python instalado.
2. Desde la raíz del repositorio, ejecuta el script:
   ```bash
   python python/make_html_files.py
   ```
3. El script creará (o actualizará) los archivos HTML en la carpeta `pages/` usando la plantilla y los contenidos definidos.

Puedes modificar los archivos de contenido en `python/body-pages/` o la plantilla base para personalizar las páginas generadas.

## Compilar archivos SCSS a CSS

Para crear y compilar un archivo `style/style-test.scss` y generar el archivo `sass-test.css`, sigue estos pasos:

1. Crea el archivo SCSS:
   ```bash
   touch  styles/style.scss 
   ```
   Escribe tu código SCSS dentro de ` styles/style.scss ` usando tu editor favorito.

2. Compila el archivo SCSS a CSS usando Sass:
   ```bash
   sass  styles/style.scss  styles/test-sass.css
   ```
   Esto generará el archivo `test-sass.css` en el mismo directorio.

3. Si quieres que Sass observe los cambios y recompile automáticamente:
   ```bash
   sass --watch styles/style.scss:styles/test-sass.css
   ```

Ahora puedes enlazar `styles/test-sass.css` en tu archivo HTML.

Para detener el proceso de observación, presiona `Ctrl + C` en la terminal.

## Cómo usar este repositorio

1. Clona el repositorio en tu máquina local.
2. Navega a las diferentes carpetas para encontrar ejemplos y ejercicios.
3. Sigue las instrucciones en los archivos README de cada carpeta para completar los ejercicios.
4. Experimenta con el código y realiza tus propias modificaciones.
5. Se recomienda usar la extensión **Live Preview** de VS Code para visualizar los cambios en tiempo real.
6. Para parar las extensiones, puedes usar el comando `Ctrl + Shift + P` y buscar "Live Preview: Stop Live Preview".
7. Si lo anterior no funciona para detener el servidor, puedes cerrar la pestaña del navegador o reiniciar VS Code.
8 Si deseas detener el servidor, puedes usar el comando `Ctrl + C` en la terminal donde se está ejecutando el servidor.
9. Si todo lo anterior no funciona,  abre la terminal y ejecuta el siguiente comando 
   ```bash
   kill $(lsof -t -i:5500)
   ```
   Esto detendrá cualquier proceso que esté utilizando el puerto 5500.
   pero si el puerto es diferente como `http://127.0.0.1:3000/`puedes cambiar el `5500` por el puerto que estés utilizando, de la siguiente manera
    ```bash
    kill $(lsof -t -i:3000)
    ```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Envía tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request en este repositorio.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue o contactar al mantenedor del proyecto.