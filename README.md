# Traductor de Documentos

¡Bienvenido al Traductor de Documentos! Esta aplicación web te permite traducir documentos en formato PDF, EPUB y TXT al español de manera rápida y sencilla.

## Características

- Soporta archivos PDF, EPUB y TXT.
- Diferentes modelos de traducción disponibles: groq, xAI, ollama.
- Opción para dividir documentos grandes en fragmentos para una traducción más eficiente.
- Interfaz de usuario intuitiva y fácil de usar.

## Requisitos

- Python 3.7 o superior.
- Librerías de Python listadas en `requirements.txt`.

## Instalación

1. Clona este repositorio en tu máquina local:

   ```sh
   git clone https://github.com/tu-usuario/traductor-de-documentos.git
   cd traductor-de-documentos
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta la aplicación:

   ```sh
   streamlit run app.py
   ```

2. Abre tu navegador web y ve a `http://localhost:8501`.

3. Sigue las instrucciones en la interfaz de usuario:
   - Sube el archivo que deseas traducir.
   - Selecciona el modelo de traducción preferido.
   - Si el documento es grande, selecciona la opción para dividir el documento en fragmentos y especifica el tamaño de los fragmentos.
   - Haz clic en el botón "Traducir" para iniciar el proceso de traducción.
   - Una vez completada la traducción, podrás descargar el documento traducido en formato PDF.

## Estructura del Proyecto

- `app.py`: Archivo principal de la aplicación que contiene la lógica de la interfaz de usuario y el flujo de trabajo de traducción.
- `readers.py`: Módulo para leer diferentes tipos de archivos.
- `chuncker.py`: Módulo para dividir texto en fragmentos.
- `model_selector.py`: Módulo para seleccionar el modelo de traducción.
- `pdf_constructor.py`: Módulo para crear archivos PDF a partir de texto.

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu nueva característica (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añade nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Crea un nuevo Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de [mi perfil de GitHub](https://github.com/jagarut).

---

¡Gracias por usar el Traductor de Documentos! Espero que te sea de gran ayuda.
