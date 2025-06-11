### 🎯 ¿Para qué sirve este programa?

Este script sirve para:

1. **Transcribir un video** (reconocer y convertir en texto lo que se dice).
2. **Traducir ese texto** a otro idioma (por ejemplo, del inglés al español).
3. **Crear subtítulos** con esa traducción.
4. **Añadir los subtítulos al video final**, dejándolos visibles permanentemente.

Ideal para crear versiones subtituladas de videos de forma automática.

---

### 🔧 Requisitos para que funcione

* Tener Python instalado.
* Instalar algunas bibliotecas con este comando:

```bash
pip install faster-whisper ffmpeg-python python-srt deep-translator
```

* Tener el programa **FFmpeg** instalado y accesible desde la consola.

---

### 🧠 ¿Qué hace cada parte del código?

#### 1. **Configuración inicial**

```python
VIDEO_INPUT = "traduciendo.mp4"     # El video que quieres subtitular
VIDEO_OUTPUT = "traduciendo_subtitulada.mp4"  # El nombre del video final con subtítulos
SRT_FILE = "subtitulos.srt"         # Archivo intermedio con los subtítulos
LANG_ORIG = "en"                    # Idioma original del video (en = inglés)
LANG_TARGET = "es"                  # Idioma al que quieres traducir (es = español)
MODEL_SIZE = "base"                 # Tamaño del modelo de transcripción (más grande = más preciso pero más lento)
```

---

#### 2. **Transcripción del audio del video**

```python
def transcribe_video(video_path):
    ...
```

Utiliza la IA Whisper (de OpenAI) para convertir el **audio del video en texto**. Devuelve segmentos de texto con marcas de tiempo.

---

#### 3. **Traducción del texto transcrito**

```python
def translate_text(text):
    ...
```

Traduce cada pedazo del texto usando **Google Translate (en modo libre y local)**. Si hay error, se marca en pantalla.

---

#### 4. **Generación del archivo de subtítulos (.srt)**

```python
def generate_translated_srt(segments, srt_path):
    ...
```

Crea un archivo `.srt` con subtítulos **traducidos**, usando los tiempos del audio original.

---

#### 5. **Incrustar subtítulos en el video**

```python
def add_subtitles_to_video(input_video, srt_file, output_video):
    ...
```

Utiliza **FFmpeg** para "quemar" los subtítulos en el video, es decir, los deja visibles permanentemente.

---

#### 6. **Flujo principal del programa**

```python
def main():
    ...
```

Este bloque ejecuta todos los pasos anteriores, uno tras otro. Solo necesitas tener el video original listo.

---

### ▶️ ¿Cómo se usa?

1. Asegúrate de que el video esté en la misma carpeta del script y se llame `traduciendo.mp4` (o cambia el nombre en `VIDEO_INPUT`).
2. Ejecuta el script:

```bash
python nombre_del_script.py
```

3. Espera a que termine. Se generará un nuevo video llamado `traduciendo_subtitulada.mp4` con los subtítulos ya añadidos.

---

### 📌 ¿Qué puedes modificar?

* Cambia `LANG_ORIG` y `LANG_TARGET` para traducir entre otros idiomas (por ejemplo, de ruso a portugués).
* Puedes usar otro modelo cambiando `MODEL_SIZE` a `"small"` o `"medium"` si quieres mejor precisión.
* Cambia el tamaño y tipo de fuente modificando los valores en `force_style` dentro de `add_subtitles_to_video`.

---

### ✅ Conclusión

Este programa es una herramienta poderosa que **automatiza todo el proceso de subtitulación y traducción de videos**, sin depender de servicios en la nube. Es ideal para creadores de contenido, educadores, o simplemente para ver videos en otros idiomas con subtítulos traducidos.
